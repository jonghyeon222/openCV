import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

if cap.isOpened():
    print("카메라 연결 성공")
else:
    print("카메라 연결 실패")
    exit()

while True:
    ret, frame = cap.read()

    if not ret: break

    out.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()