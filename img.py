import cv2
import numpy as np
img=cv2.imread('ph1.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitkey(0)
cv2.destroyAllwindows()
