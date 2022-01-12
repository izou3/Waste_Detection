import cv2
import os 
import sys
from videos import env

path = r"D:\West_Village_Waste_Footage\11-16-2021\Front-Trash-Can\2021\11\16\Val7.h264"
MASKRCNN_MODEL = r"C:\Users\IvanZou\OneDrive\Documents\OpenCV_Python3\Waste_Detection\weights"


cap = cv2.VideoCapture(path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) / 2)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) / 2)
frames_per_second = cap.get(cv2.CAP_PROP_FPS)
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print('Num Frames ', float(num_frames))
print("fps ", frames_per_second)
print("width ", width)
print("height ", height)
print("fourcc ", cv2.VideoWriter_fourcc(*"MJPG"))
# Initialize video writer
video_writer = cv2.VideoWriter('out.avi', cv2.VideoWriter_fourcc(*'XVID'), fps=float(frames_per_second), frameSize=(width, height), isColor=True)

counter = 0

while(cap.isOpened()):
    if counter > 50:
      break

    ret, frame = cap.read()
    if ret==True:

        # write the flipped frame
        video_writer.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    counter = counter + 1

cap.release()
video_writer.release()
cv2.destroyAllWindows()
