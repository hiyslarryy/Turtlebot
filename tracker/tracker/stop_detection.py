#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import cv2
import numpy as np

def crop_frame(image):
    height, length, _ = image.shape
    return image[0: height//3*2, 0: length]

class StopSignDetector(Node):
    def __init__(self):
        super().__init__('stop_sign_detector')
        self.publisher_ = self.create_publisher(Bool, 'stop_sign_detected', 10)
        self.timer = self.create_timer(0.1, self.detect_stop_sign)
        self.cap = cv2.VideoCapture(1)
        self.stop_sign_cascade = cv2.CascadeClassifier('/home/hiyslarry/ros2_ws/src/tracker/tracker/stop_sign_classifier_2.xml')

    def detect_stop_sign(self):
        ret, frame = self.cap.read()
        if ret:
            cropped_frame = crop_frame(frame)
            img_filter = cv2.GaussianBlur(cropped_frame, (5, 5), 0)
            gray_filtered = cv2.cvtColor(img_filter, cv2.COLOR_BGR2GRAY)
            stop_signs = self.stop_sign_cascade.detectMultiScale(gray_filtered, scaleFactor=1.05, minNeighbors=15, minSize=(30, 30))
            stop_detected = len(stop_signs) > 0
            self.publisher_.publish(Bool(data=stop_detected))

            if stop_detected:
                for (x, y, w, h) in stop_signs:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == 27:  # ESC key to exit
                self.cap.release()
                cv2.destroyAllWindows()
                rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    stop_sign_detector = StopSignDetector()
    rclpy.spin(stop_sign_detector)
    stop_sign_detector.destroy_node()

if __name__ == '__main__':
    main()
