import cv2 as cv
import numpy as np
import mediapipe as mp



mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
cap = cv.VideoCapture(1)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:
    while True:
        worked, frame = cap.read()
        if worked:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            results = hands.process(frame)
            frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmark in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmark, connections=mp_hands.HAND_CONNECTIONS)
            cv.imshow("frame", frame)
        key = cv.waitKey(5) & 0xFF
        if key == 27:
            break
cv.destroyAllWindows()



