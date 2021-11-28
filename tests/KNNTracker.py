import cv2
import root
import numpy as np
from videos import env

OPENCV_MAJOR_VERSION = int(cv2.__version__.split('.')[0])

bg_subtractor = cv2.createBackgroundSubtractorKNN(detectShadows=True)

erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 5))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 11))

# path = env._ABSOLUTE_PATH + r"\TestVideo5.h264"
path = r"D:\West_Village_Waste_Footage\11-16-2021\Front-Trash-Can\2021\11\16\TestVideoY.h264"
cap = cv2.VideoCapture(path)
success, frame = cap.read()

print("Detecting circle")
# Detect the circle
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
rows = gray.shape[0]
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=0)

while success:

    fg_mask = bg_subtractor.apply(frame)

    _, thresh = cv2.threshold(fg_mask, 244, 255, cv2.THRESH_BINARY)
    cv2.erode(thresh, erode_kernel, thresh, iterations=2)
    cv2.dilate(thresh, dilate_kernel, thresh, iterations=2)

    if OPENCV_MAJOR_VERSION >= 4:
        # OpenCV 4 or a later version is being used.
        contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                          cv2.CHAIN_APPROX_SIMPLE)
    else:
        # OpenCV 3 or an earlier version is being used.
        # cv2.findContours has an extra return value.
        # The extra return value is the thresholded image, which is
        # unchanged, so we can ignore it.
        _, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) > 5000:
            x, y, w, h = cv2.boundingRect(c)
            if (y != 0):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)  # last 2 args are color and border width of rectangle 

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            radius = i[2]
            cv2.circle(frame, center, radius, (255, 0, 255), 3)

    # cv2.imshow('knn', fg_mask)
    # cv2.imshow('thresh', thresh)
    resize = cv2.resize(frame, (600, 400))
    cv2.imshow('detection', resize)

    k = cv2.waitKey(30)
    if k == 27:  # Escape
        break

    success, frame = cap.read()