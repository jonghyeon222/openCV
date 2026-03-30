import cv2
import numpy as np

def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            if flags & cv2.EVENT_FLAG_LBUTTON:
                cv2.line(canvas, (x, y), (x, y), (0, 0, 0), 3)
                cv2.imshow("canvas", canvas)


canvas = np.full((512, 512, 3), 255, np.uint8)

cv2.imshow("canvas", canvas)
cv2.setMouseCallback("canvas", mouse_callback)

while True:
    key = cv2.waitKey(0) & 0xFF
    if  key == ord('q') or key == 27:
        cv2.destroyAllWindows()
        break
    elif key == ord('c'):
        canvas = np.full((512, 512, 3), 255, np.uint8)
        cv2.imshow("canvas", canvas)