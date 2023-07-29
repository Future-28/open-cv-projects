import cv2 as cv
import sys
import numpy as np

# create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 pixel
# cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# cv.rectangle(img, (384, 20), (510, 258), (0, 255, 0), 3)
cv.circle(img,(447,63), 63, (0,0,255), -1)
cv.imshow("line", img)

cv.waitKey(0)
cv.destroyWindow()


