import cv2
import numpy as np

img = cv2.imread("../rail.jpg")
img_copy = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0)
edges = cv2.Canny(blur, 50, 150)

# 차선은 주로 하단에 있다. 이미지를 반 자르기 방식 활용가능
# rows, cols = edges.shape
# edges = edges[rows//2:, :]

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 210, minLineLength=250, maxLineGap=40)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)


cv2.imshow("img", img)
cv2.imshow("edges", edges)
cv2.imshow("img_copy", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()