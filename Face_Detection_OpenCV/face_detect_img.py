import cv2
import sys
import argparse

def face_detect(image, faceCascade):
    if len(image.shape)==3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(gray, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    return faces


def draw_face_boxes(image, faces):
    if faces is None:
        return image
    for (x, y, w, h) in faces:
        print("Drawing rectangle (x, y, w, h) = ({0}, {1}, {2}, {3})".format(x, y, w, h))
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return image



# Get user supplied values
imagePath = 'data/test_image.png'
cascPath = 'model/haarcascade_frontalface_default.xml'
image = cv2.imread(imagePath)

if image is None:
    print ("Image is not found!")
else:
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)
    faces = face_detect(image, faceCascade)
    print("Found {0} faces!".format(len(faces)))
    
    # Draw rectangles around all faces (if any)
    output_image = draw_face_boxes(image, faces)
    
    # Save output
    output_name = imagePath.replace(".", "_out.")
    cv2.imwrite(output_name, image)
    
    
    
