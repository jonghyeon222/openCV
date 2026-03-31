import cv2
import numpy as np

img = cv2.imread("../coins.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY_INV, blockSize=57, C=1)

kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

contours, hierachy = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

result = cv2.drawContours(img, contours, -1, (0,255,0), 3)

result = cv2.putText(result, f"coin count: {len(contours)}", (0,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)


cv2.imshow("edges", blur)
cv2.imshow("thresh", thresh)
cv2.imshow("morph", morph)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()