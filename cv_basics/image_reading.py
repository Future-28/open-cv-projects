import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("aisle.jpg"))

if img is None:
    sys.exit("Image not found.")

cv.imshow("Display Window", img)
# waits a key from keyboard and stores in k
k = cv.waitKey(0)

# if users press the s , imwrite saves image as png
if k == ord("s"):
    cv.imwrite("aisle.png", img)

cv.destroyWindow()