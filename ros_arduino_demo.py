#!/usr/bin/env python

import rospy
from ros_arduino_msgs.srv import *
from sensor_msgs.msg import Range

changeLed = rospy.ServiceProxy('/arduino/analog_write', AnalogWrite) 
#changes led brightness

pin = 6 #Pin for LED
dist = 0 #distance
									
def callback(data):
	rospy.loginfo(rospy.get_caller_id() + ": Entfernung: %s meter", data.range)
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
	rospy.init_node("ros_arduino_demo")#name
	rospy.Subscriber("/arduino/sensor/ir_front_center", Range, callback)#subscribe to get data
	rospy.spin()#Loop

if __name__ == '__main__':
	listen()
