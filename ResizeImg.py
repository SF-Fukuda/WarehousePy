import cv2
import numpy as numpy

img = cv2.imread('Python.png',1)

height = int(img.shape[0] /4)
width = int(img.shape[1] / 4)

reImg = cv2.resize(img,(width,height))

cv2.imshow('img', reImg)
cv2.waitKey(0)
cv2.destroyAllWindows()