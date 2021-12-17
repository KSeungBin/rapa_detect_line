import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge  # 자동으로 ros의 image message를 opencv가 사용하는 데이터로 바꿔줌
bridge = CvBridge()      # 인스턴스화한 후 callback 내부에서 사용하기

# ROS Image를 opencv로 받기
def callback(image_data):
    cv_image = bridge.imgmsg_to_cv2(image_data, 'bgr8')  # opencv는 rgb가 아닌 bgr로 바꿔줘야 함, 8bit로 비트 수는 맞춰주기
    cv.imshow('callback', cv_image)
    cv.waitKey(1)  # callback이 계속 들어오기 때문에 숫자를 크게 주면 안됨
    pass

rospy.init_node('img_cv_node')
rospy.Subscriber('/cv_camera/image_raw', Image, callback)  # publish하는 것은 당연히 callback이 있다
rospy.spin()    # 주기적으로 받는 건 spin. sensor에서 날아오는 frame은 sensor만 알 수 있다.

