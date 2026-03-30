import cv2
import numpy as np

sonic = cv2.imread("../green.jpg")
sonic = cv2.resize(sonic, (512,512))
hsv1 = cv2.cvtColor(sonic, cv2.COLOR_BGR2HSV)

lena = cv2.imread("../lena.jpg")
hsv2 = cv2.cvtColor(lena, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 50, 50])
upper_green = np.array([90, 255, 255])

mask1 = cv2.inRange(hsv1, lower_green, upper_green)
green = cv2.bitwise_and(sonic, sonic, mask=mask1)
mask2 = cv2.bitwise_not(mask1)
char = cv2.bitwise_and(sonic, sonic, mask=mask2)

lena_sonic = cv2.bitwise_and(lena, lena, mask=mask1)
lena_sonic_final = cv2.bitwise_or(lena_sonic, char)



cv2.imshow("img1", char)
cv2.imshow("img2", green)
cv2.imshow("img3", mask1)
cv2.imshow("img4", lena_sonic)
cv2.imshow("img5", lena_sonic_final)
cv2.waitKey(0)
cv2.destroyAllWindows()