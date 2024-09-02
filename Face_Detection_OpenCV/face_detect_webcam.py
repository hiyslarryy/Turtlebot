import cv2
import argparse
from time import sleep

# reuse the packages you wrote
from face_detect_img import face_detect, draw_face_boxes


faceCascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)

# your program loop
while True:
    if video_capture.isOpened():
        ret, frame = video_capture.read()
        frame_resized =  cv2.resize(frame,(640,480))
        faces = face_detect(frame_resized, faceCascade)
        image_out = draw_face_boxes(frame_resized, faces)

        # Display the resulting frame
        cv2.imshow('Output', image_out)

        # Press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When done, release the capture
video_capture.release()
cv2.destroyAllWindows()
