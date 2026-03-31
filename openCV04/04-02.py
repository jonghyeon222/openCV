import cv2
import numpy as np

img = cv2.imread('../lena.jpg')

# 임계값 조절이 중요합니다. (보통 1:2 또는 1:3 비율 사용)
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Canny Edge', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()