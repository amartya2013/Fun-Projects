import cv2
import numpy as np


capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret: break
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (17, 17), 0)
    cv2.imshow("Camera", blur)
    circles = cv2.HoughCircles(
        blur,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=200,
        param1=100,
        param2=60,
        minRadius=100,
        maxRadius=250
    )
    if circles is not None:
        np_circles = np.uint16(np.around(circles))
        for i in np_circles[0,:]:
            # draw the outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow('detected circles', frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()