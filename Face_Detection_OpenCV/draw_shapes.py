import cv2 as cv2
import numpy as np

BLACK = (0, 0, 0)  # all zeros
WHITE = (255, 255, 255) # all ones (*255)

# in OpenCV, the default is BGR
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

# remember, the top-left corner is (0, 0)
p0 = 100, 210
p1 = 500, 590

p2 = 600, 220    
p3 = 850, 380

img = cv2.imread('data/Turtles.png')# input image
print(img.shape)

resized_img = cv2.resize(img, (960, 640))
print(resized_img.shape)


# Draw rectangles on the canvas
cv2.rectangle(resized_img, p0, p1, BLUE, 2)
cv2.rectangle(resized_img, p2, p3, RED, cv2.FILLED)


# Show the image on a window
cv2.imshow('Window Name', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image
cv2.imwrite('data/output_turtles.png', resized_img)
