import cv2 as cv
import sys
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open the camera")
    exit()

while True:
    # Capture frame by frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame. Exiting ...")
        break

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything is done, release the capture
cap.release()
cv.destroyWindow()


