import cv2
import numpy as np
import os

FIND_CIRCLE_MODE=False

filename = "frame212_11-17_1951_Front.jpg"
path = r"C:\Users\IvanZou\OneDrive\Documents\OpenCV_Python3\Waste_Detection\images\All_Images\frame212_11-17_1951_Front.jpg"

write_directory = r"C:\Users\IvanZou\OneDrive\Documents\OpenCV_Python3\Waste_Detection\images\Manual_Mask"

img = cv2.imread(path)
img = cv2.resize(img, (920, 540))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.medianBlur(gray, 25) #cv2.bilateralFilter(gray,10,50,50)

# Tuned Circle Parameter to find optimal circle. Will likely need to tune for 
# each individual image
minDist = 300
param1 = 50 #500
param2 = 30 #200 #smaller value-> more false circles
minRadius = 100
maxRadius = 500 #10

circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

if (FIND_CIRCLE_MODE):
  if circles is not None:
      circles = np.uint16(np.around(circles))
      for i in circles[0,:]:
        # if (i[0] < 600 and i[0] > 300 and i[1] > 250 and i[1] < 600): 
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)

if (not FIND_CIRCLE_MODE):
  circles = np.uint16(np.around(circles))
  optimal_circle = circles[0][0]   # set to the optimal circle found

  cv2.circle(img, (optimal_circle[0], optimal_circle[1]), optimal_circle[2], (0, 0, 0), 2)

  mask = np.zeros_like(img)
  mask = cv2.circle(mask, (optimal_circles[0], optimal_circle[1]), optimal_circle[2], (255,255,255), -1)

  # # # apply mask to image
  result = cv2.bitwise_and(img, mask)

  # # write result
  os.chdir(write_directory)
  cv2.imwrite(filename, result)
else:
  # Show result for testing:
  cv2.imshow('images', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
