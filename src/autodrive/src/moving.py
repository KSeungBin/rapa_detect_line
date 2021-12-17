#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist


rospy.init_node('moving')
pub = rospy.Publisher('/turtlebot3_core/cmd_vel', Twist, queue_size=10) # 제일 중요한 기본 포맷 rospy.Publisher('hello_pub', String, queue_size=)
twist = Twist()

def move(msg):
    twist.linear.x = 0.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.0
    if msg=='w':
        twist.linear.x = 1.0
        twist.angular.z = 0.0
    elif msg=='a':
        twist.linear.x = 1.0
        twist.angular.z = -1.0
    elif msg=='d':
        twist.linear.x = 1.0
        twist.angular.z = 1.0
    elif msg=='x':
        twist.linear.x = -1.0
        twist.angular.z = 0.0
    elif msg=='s':
        twist.linear.x = 0.0
        twist.angular.z = 0.0
    pub.publish(twist)
    


