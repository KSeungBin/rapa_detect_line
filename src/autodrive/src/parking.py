#! /usr/bin/ python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np
import math
# scan -> callback

def turn90(direction):
    if direction=="left":
        relative_angle = math.radians(10)
        angular_speed = 1.0
        duration = relative_angle /angular_speed
        time2end = rospy.Time.now() + rospy.Duration(duration)
        msg = Twist()
        msg.angular.z = angular_speed
        while rospy.Time.now() < time2end:
            pub.publish(msg)
            rospy.sleep(0.01)
    elif direction=="right":
        relative_angle = math.radians(10)
        angular_speed = 1.0
        duration = relative_angle /angular_speed
        time2end = rospy.Time.now() + rospy.Duration(duration)
        msg = Twist()
        msg.angular.z = -angular_speed
        while rospy.Time.now() < time2end:
            pub.publish(msg)
            rospy.sleep(0.01)
    print(direction)

def callback(data):
    global pub
    NUM = 0.2
    laser_front = np.array(data.ranges[-30:]+data.ranges[:30])
    laser_range1 = np.array(data.ranges[89:90]) # 정면 부분
    laser_range2 = np.array(data.ranges[-90:-89]) # 정면 부분
    left_val = np.sum(laser_range1[laser_range1>0])
    right_val = np.sum(laser_range2[laser_range2>0])
    front_val = np.mean(laser_front[laser_front>0])
    cmd_vel = Twist()
    if front_val<0.5 and front_val>0:
        cmd_vel.linear.x = 0.0
        pub.publish(cmd_vel)
        rospy.sleep(0.01)
        if right_val<left_val:
            turn90('right')
        elif right_val>=left_val:
            turn90('left')
        
    else:
        if right_val>left_val*NUM and right_val*left_val>0:
            cmd_vel.linear.x = 0.1
            cmd_vel.angular.z = 0.5
        elif right_val<=left_val*NUM and right_val*left_val>0:
            cmd_vel.linear.x = 0.1
            cmd_vel.angular.z = -0.5
        else:
            cmd_vel.linear.x = 0.1
            cmd_vel.angular.z = 0.0

        pub.publish(cmd_vel)
    print(front_val,left_val, right_val)
    rospy.sleep(0.01)
    pass

def main():
    rospy.init_node('parking')
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()
    pass

if __name__ == "__main__":
    pub = rospy.Publisher('/cmd_vel', Twist,queue_size=1)
    main()
    