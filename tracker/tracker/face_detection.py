#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class FaceDetectionNode(Node):
    def __init__(self):
        super().__init__('face_detection_node')
        self.publisher_ = self.create_publisher(Image, 'detected_faces', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.cap = cv2.VideoCapture(1)
        self.bridge = CvBridge()
        self.face_cascade = cv2.CascadeClassifier('/home/hiyslarry/ros2_ws/xml/haarcascade_frontalface_default.xml')

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv_image = self.bridge.cv2_to_imgmsg(frame, 'bgr8')
            self.publisher_.publish(cv_image)
            cv2.imshow('Face Detection', frame)
            cv2.waitKey(1)

    def destroy_node(self):
        cv2.destroyAllWindows()
        self.cap.release()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    face_detection_node = FaceDetectionNode()

    try:
        rclpy.spin(face_detection_node)
    except KeyboardInterrupt:
        pass
    finally:
        face_detection_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
