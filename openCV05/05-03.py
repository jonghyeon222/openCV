import cv2
import numpy as np

img = cv2.imread('../morphology.jpg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)

result1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
result2 = cv2.morphologyEx(result1, cv2.MORPH_CLOSE, kernel)

cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)
cv2.waitKey(0)
cv2.destroyAllWindows()