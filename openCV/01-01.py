import cv2
import numpy as np
import sys

img = cv2.imread("lena.jpg")

print(img.shape)

if img is None:
    print("이미지 없음")
    sys.exit()

blue = img[100, 100, 0]
green = img[100, 100, 1]
red = img[100, 100, 2]

print("100행 100열의 색상:", blue, green, red)

img[100, 100] = [0, 0, 0]

cv2.imshow("lena", img)
cv2.waitKey(0)
cv2.destroyAllWindows()