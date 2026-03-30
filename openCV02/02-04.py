import cv2

img = cv2.imread("../lena.jpg")

b,g,r = cv2.split(img)

dst = cv2.merge((b, g, r))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)
cv2.imshow("merge", dst)
cv2.imshow("hsv", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()