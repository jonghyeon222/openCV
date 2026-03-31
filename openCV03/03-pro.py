import cv2
import numpy as np

points = []

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img_copy, (x,y), 4, (0,0,255), 2)
        points.append((x,y))
        print(x,y)
        cv2.imshow("img",img_copy)

        if len(points) == 4:
            resize_img()

def resize_img():
    pts1 = np.float32([points[0], points[1], points[2], points[3]])
    pts2 = np.float32([[0, 0], [347, 0], [347, 280], [0, 280]])

    t_a = cv2.getPerspectiveTransform(pts1, pts2)
    wps = cv2.warpPerspective(img, t_a, (cols, rows), flags=cv2.INTER_LANCZOS4)

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    dst = cv2.filter2D(wps, -1, kernel)

    cv2.imshow("dst", dst)
    print("수정 이미지 출력, 좌표:", points)

img = cv2.imread("../football-field.jpg")
img_copy = img.copy()
rows,cols,channels = img.shape

cv2.imshow("img",img)
cv2.setMouseCallback("img",mouse_click)

cv2.waitKey(0)
cv2.destroyAllWindows()