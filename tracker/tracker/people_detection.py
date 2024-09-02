#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import imutils

class PeopleDetectionNode(Node):
    def __init__(self):
        super().__init__('people_detection_node')
        self.publisher_ = self.create_publisher(Image, 'detected_people', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.cap = cv2.VideoCapture(1)
        self.bridge = CvBridge()
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            frame = imutils.resize(frame, width=min(400, frame.shape[1]))
            regions, _ = self.hog.detectMultiScale(frame, winStride=(4, 4), padding=(4, 4), scale=1.05)

            for (x, y, w, h) in regions:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv_image = self.bridge.cv2_to_imgmsg(frame, 'bgr8')
            self.publisher_.publish(cv_image)
            cv2.imshow('People Detection', frame)
            cv2.waitKey(1)

    def destroy_node(self):
        cv2.destroyAllWindows()
        self.cap.release()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    people_detection_node = PeopleDetectionNode()

    try:
        rclpy.spin(people_detection_node)
    except KeyboardInterrupt:
        pass
    finally:
        people_detection_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
