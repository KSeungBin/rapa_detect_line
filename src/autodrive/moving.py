#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10) # 제일 중요한 기본 포맷 rospy.Publisher('hello_pub', String, queue_size=)

def move(msg):
    global pub
    msg = msg.data
    twist = Twist()
    twist.linear.x = 0.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.0
    if msg=='w':
        twist.linear.x = 0.5
        twist.angular.z = 0.0
    elif msg=='a':
        twist.linear.x = 0.5
        twist.angular.z = -1.0
    elif msg=='d':
        twist.linear.x = 0.5
        twist.angular.z = 1.0
    elif msg=='x':
        twist.linear.x = -0.5
        twist.angular.z = 0.0
    elif msg=='s':
        twist.linear.x = 0.0
        twist.angular.z = 0.0
    else:
        pass
    pub.publish(twist)

if __name__ == "__main__":
    rospy.init_node('moving')
    rospy.Subscriber('get_order', String, callback=move)
    rospy.spin()
