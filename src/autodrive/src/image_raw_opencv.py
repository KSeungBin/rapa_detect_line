import rospy
import cv2 as cv
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge  # 자동으로 ros의 image message를 opencv가 사용하는 데이터로 바꿔줌
bridge = CvBridge()      # 인스턴스화한 후 callback 내부에서 사용하기
pub = rospy.Publisher('get_order', String, queue_size=10)

# ROS Image를 opencv로 받기
def callback(image_data):
    cv_image = bridge.imgmsg_to_cv2(image_data, 'bgr8')  # opencv는 rgb가 아닌 bgr로 바꿔줘야 함, 8bit로 비트 수는 맞춰주기
    img_gray = cv.cvtColor(cv_image, cv.COLOR_BGR2GRAY)
    imgG = img_gray/255.
    imgG = np.round(imgG)
    cal = imgG[400:480,240:400]
    most_val = -1
    most_direction = -1
    for i in range(8):
        if i ==0:
            most_val = np.sum(cal[:,i*20:(i+1)*20])
            most_direction = 0
        else:
            tmp_val = np.sum(cal[:,i*20:(i+1)*20])
            if most_val>tmp_val:
                most_val=tmp_val
                most_direction=i
    if most_direction <3:
        msg = 'a'
    elif most_direction >5:
        msg = 'd'
    else:
        msg = 'w'
    imgG = imgG*255.
    cv.imshow('callback', imgG)
    print(msg)
    cv.waitKey(1)  # callback이 계속 들어오기 때문에 숫자를 크게 주면 안됨
    pub.publish(msg)
    pass

rospy.init_node('img_cv_node')
rospy.Subscriber('/cv_camera/image_raw', Image, callback)  # publish하는 것은 당연히 callback이 있다
rospy.spin()    # 주기적으로 받는 건 spin. sensor에서 날아오는 frame은 sensor만 알 수 있다.

