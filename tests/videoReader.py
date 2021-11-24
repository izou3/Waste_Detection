import numpy as np
import cv2

import root
from videos import env

# path
path = env._ABSOLUTE_PATH + r"\testVideo1.h264"

cap = cv2.VideoCapture(path)

if (cap.isOpened() == False):
    print("Error Opening Video Stream/file")
    
while (cap.isOpened()):
    ret, frame = cap.read();
    if (ret == True):
        cv2.imshow('Frame', frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
# Closes all the frames
cv2.destroyAllWindows()

# image = cv2.imread(path)
# # Displaying the image
# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.imwrite('tew.jpg', image)