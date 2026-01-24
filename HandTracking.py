import cv2 as cv
import mediapipe as mp

mp_hands = mp.solutions.hands
cap = cv.VideoCapture(0)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:

    while True:
        worked, frame = cap.read()
        if not worked:
            break

        h, w, _ = frame.shape

        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                # Landmark 0 = wrist
                lm0 = hand_landmarks.landmark[0]

                cx = int(lm0.x * w)
                cy = int(lm0.y * h)

                # Red dot
                cv.circle(frame, (cx, cy), 8, (0, 0, 255), -1)

        cv.imshow("frame", frame)

        if cv.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv.destroyAllWindows()




