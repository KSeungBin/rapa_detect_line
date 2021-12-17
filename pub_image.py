#! /usr/bin/env python3
import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
bridge =  CvBridge()


def callback(image_data):
    cv_image = bridge.imgmsg_to_cv2(image_data, 'bgr8')
    cv.imshow('callback', cv_image)
    cv.waitKey(1)
    cv.imwrite('road_detect.png', cv_image, params=[cv.IMWRITE_PNG_COMPRESSION,0])
    cv.waitKey(1)
    pass


if __name__ == '__main__':
    rospy.init_node('img_cv_node') 
    pub = rospy.Publisher('hello', Image, queue_size=10) 
    spin = rospy.spin()  
    pass

