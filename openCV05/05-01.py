import cv2
import numpy as np

src = cv2.imread('../lena.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow('Red Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()