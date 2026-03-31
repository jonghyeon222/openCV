import cv2
import numpy as np

img = cv2.imread('../lena.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv2.equalizeHist(img)

cv2.imshow('img', img)
cv2.imshow('equalized', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()