import cv2
import numpy as np
import os

# Tuned Circle Parameter to find optimal circle. Will likely need to tune for 
# each individual image
minDist = 100
param1 = 30 #500
param2 = 50 #200 #smaller value-> more false circles
minRadius = 200
maxRadius = 1000 #10

read_directory = r'C:\Users\IvanZou\OneDrive\Documents\OpenCV_Python3\Waste_Detection\images\Test_Set'
write_directory = r'C:\Users\IvanZou\OneDrive\Documents\OpenCV_Python3\Waste_Detection\images\Masked_Test'

for filename in os.listdir(read_directory):
  if filename.endswith(".jpg") or filename.endswith(".png"):
    path = os.path.join(read_directory, filename)

    img = cv2.imread(path)
    img = cv2.resize(img, (920, 540))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred = cv2.medianBlur(gray, 25) #cv2.bilateralFilter(gray,10,50,50)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    if circles is None: 
      print(filename)
      continue

    max_area_i = []
    max_area = 0
    if circles is not None:
      circles = np.uint16(np.around(circles))
      for i in circles[0,:]:
        print(circles)
        # if (((i[0] < 800 and i[0] > 200) or (i[1] > 100 and i[1] < 800)) and (i[2] > 200 and i[2] < 300)): 
        if ((i[0] < 600) and (i[1] > 200)):
          area = 3.14 * i[2] * i[2]
          if area > max_area:
            max_area_i = i
            max_area = area

    cv2.circle(img, (max_area_i[0], max_area_i[1]), max_area_i[2], (0, 0, 0), 2)

    mask = np.zeros_like(img)
    mask = cv2.circle(mask, (max_area_i[0], max_area_i[1]), max_area_i[2], (255,255,255), -1)

    # apply mask to image
    result = cv2.bitwise_and(img, mask)

    os.chdir(write_directory)
    cv2.imwrite(filename, result)

  else:
    continue