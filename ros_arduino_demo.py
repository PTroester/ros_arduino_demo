#!/usr/bin/env python

import rospy
from ros_arduino_msgs.srv import *
#Service einbinden
from sensor_msgs.msg import Range
#Range msg einbinden

changeLed = rospy.ServiceProxy('/arduino/analog_write', AnalogWrite) 
#mit changeLed(pin, value) wird der rosservice aufgerufen

pin = 6 #Pin für die LED, muss PWM pin sein
dist = 0 #distanz
									
def callback(data):#callback wird in listen von rospy.Subscriber aufgerufen
	rospy.loginfo(rospy.get_caller_id() + ": Entfernung: %s meter", data.range)
	#Entfernung ausgeben
	dist = data.range
	if dist < 0.2:
		changeLed(pin, 1)
	elif dist < 0.3:
		changeLed(pin, 35)
	elif dist < 0.4:
		changeLed(pin, 70) 
	elif dist < 0.5:
		changeLed(pin, 105)
	elif dist < 0.6:
		changeLed(pin, 140)
	elif dist < 0.7:
		changeLed(pin, 175)
	elif dist < 0.8:
		changeLed(pin, 210)
	else:
		changeLed(pin, 255)


def listen():
	rospy.init_node("ros_arduino_demo")#Name des Nodes
	rospy.Subscriber("/arduino/sensor/ir_front_center", Range, callback)
	#daten von ros_arduino_bridge abrufen
	rospy.spin()#Loop Funktion

if __name__ == '__main__':
	listen()
