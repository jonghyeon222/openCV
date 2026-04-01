import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("카메라 연결 성공")
else:
    print("카메라 연결 실패")
    exit()

points = []
color = [[30,100,100], [80,255,255]]
color_mode = 1
line_color = (0, 255, 0)

def color_print(f_m, c_r):
    hsv = cv2.cvtColor(f_m, cv2.COLOR_BGR2HSV)
    lower = np.array(c_r[0])
    upper = np.array(c_r[1])
    mask = cv2.inRange(hsv, lower, upper)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=1)
    return mask

def get_xy(m_k):
    contours, hierachy = cv2.findContours(m_k, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            return (cx, cy)
    return None

def draw_lines(f_m, pts, alpha, l_c):
    canvas = np.zeros_like(f_m)
    for i in range(1, len(pts)):
        if points[i - 1] is None or points[i] is None:
            continue
        cv2.line(canvas, pts[i - 1], pts[i], l_c, 2)
    res = cv2.addWeighted(f_m, 1, canvas, alpha, 0)
    return res

def change_color(c_m, l_c):
    if c_m == 1:
        c_r = [[30,100,100], [80,255,255]]
        l_c = (0, 255, 0)
    elif c_m == 2:
        c_r = [[100,100,100], [130,255,255]]
        l_c = (255, 0, 0)
    elif c_m == 3:
        c_r = [[140,100,100], [180,255,255]]
        l_c = (0, 0, 255)

    return c_r, l_c

while True:
    ret, frame = cap.read()

    frame_copy = cv2.flip(frame, 1)

    mask = color_print(frame_copy, color)

    point = get_xy(mask)

    points.append(point)

    if len(points) > 2:
        frame_copy = draw_lines(frame_copy, points, 0.8, line_color)

    cv2.imshow("frame", frame_copy)
    cv2.imshow("mask", mask)
    key_input = cv2.waitKey(20) & 0xFF
    if key_input == 27:
        break
    elif key_input == ord('c'):
        points = []
    elif key_input == ord('p'):
        points = []
        color_mode += 1
        if color_mode >= 4:
            color_mode = 1
        color, line_color = change_color(color_mode, line_color)



cv2.destroyAllWindows()