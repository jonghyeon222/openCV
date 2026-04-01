import cv2

cap = cv2.VideoCapture(0)

tiger = cv2.imread("../tigermask.png", cv2.IMREAD_UNCHANGED)

b, g, r, a = cv2.split(tiger)
_, mask = cv2.threshold(a, 0, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

mask_rgb = cv2.merge((b, g, r))

if cap.isOpened():
    print("카메라 연결 성공")
else:
    print("카메라 연결 실패")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    face = face_cascade.detectMultiScale(frame, scaleFactor=1.08, minNeighbors=7)

    for (x, y, w, h) in face:
        mask_re = cv2.resize(mask, (int(w*2), int(h*2)))
        mask_inv_re = cv2.resize(mask_inv, (int(w*2), int(h*2)))
        mask_rgb_re = cv2.resize(mask_rgb, (int(w*2), int(h*2)))

        nx = x - int(w * 0.5)
        ny = y - int(h * 0.5)

        nx = max(nx, 0)
        ny = max(ny, 0)

        roi = frame[ny : ny+int(h*2), nx : nx+int(w*2)]

        mask_re = cv2.resize(mask_re, (roi.shape[1], roi.shape[0]))
        mask_inv_re = cv2.resize(mask_inv_re, (roi.shape[1], roi.shape[0]))
        mask_rgb_re = cv2.resize(mask_rgb_re, (roi.shape[1], roi.shape[0]))

        mask_roi = cv2.bitwise_and(roi, roi, mask=mask_inv_re)
        mask_item = cv2.bitwise_and(mask_rgb_re, mask_rgb_re, mask=mask_re)
        dst = cv2.add(mask_roi, mask_item)

        frame[ny : ny+roi.shape[0], nx : nx+roi.shape[1]] = dst

        cv2.imshow("frame", frame)
        if cv2.waitKey(30) & 0xFF == 27:
            break

    cv2.destroyAllWindows()