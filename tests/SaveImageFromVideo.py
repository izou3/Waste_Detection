import cv2
import root
from videos import env

path = r"D:\West_Village_Waste_Footage\11-17-2021\Front-Forward-Camera\2021\11\17\TestVideoF.h264"

cap = cv2.VideoCapture(path)
success, frame = cap.read()

count = 0
# print(cap.get(cv2.CAP_PROP_FPS))
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while success:    
  success,image = cap.read()
  # print('Read a new frame: ', success)
  if (count > 0 and count % 240 == 0):
    print(count)
    cv2.imwrite(r"C:\Users\IvanZou\OneDrive\Documents\OpenCV_Python3\Waste_Detection\images\11-17_2021_Front\frame%d.jpg" % int(count/60), image)     # save frame as JPEG file  
  count += 1

print(count)
# image = cv2.imread('frame1.jpg')
# print(image.shape)
# image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))
# cv2.imshow('diff', image)

# k = cv2.waitKey(0)
# if k == 27:  # Escape
#   break