import cv2
import root
from videos import env

path = r"D:\West_Village_Waste_Footage\11-16-2021\Front-Trash-Can\2021\11\16\Val7.h264"

cap = cv2.VideoCapture(path)
success, frame = cap.read()

count = 0
_SAVE_FRAME_NUMBER=240

while success:    
  success,image = cap.read()
  # print('Read a new frame: ', success)
  if (count > 0 and count % _SAVE_FRAME_NUMBER == 0):
    print(count)
    cv2.imwrite(r"C:\Users\IvanZou\OneDrive\Documents\OpenCV_Python3\Waste_Detection\images\11-17_1851_Front\frame%d_11-16_1934_Front.jpg" % int(count/60), image)     # save frame as JPEG file  
  count += 1
