import cv2
import numpy as np

img = cv2.imread('../shape.webp', cv2.IMREAD_GRAYSCALE)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100, param1=110, param2=20, minRadius=10, maxRadius=250)
dst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles:
        x1, y1, rd = circle[0]
        cv2.circle(dst, (x1, y1), rd, (0, 255, 0), 2)


cv2.imshow("img", img)
cv2.imshow("dst", dst)
print(circles)
cv2.waitKey(0)
cv2.destroyAllWindows()