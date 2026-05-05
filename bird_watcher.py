import cv2
from ultralytics import YOLO
from datetime import datetime
import os
from emailer import send_email


print("Loading YOLO model...")
model = YOLO("yoloe-11s-seg.pt")
print("Done Loading Model")



names = ["blue bird", "black bird", "red bird"]

for name in names:
    if not os.path.exists(name.replace(" ", "_")):
        os.mkdir(name.replace(" ", "_"))


model.set_classes(names, model.get_text_pe(names))
capture = cv2.VideoCapture(2)

while True:
    ret, frame = capture.read()
    if ret:
        results = model.predict(frame)
        result = results[0]

        for box in result.boxes:
            class_id = int(box.cls[0])  # numeric class (e.g., 0, 1, 2)
            label = result.names[class_id]  # human-readable label (e.g., "person")

            if label == "blue bird":
                if len(os.listdir("blue_bird")) < 20:
                    cv2.imwrite(f"blue_bird/bluebird_{datetime.now()}.jpg", frame)
                    send_email("lopamudra.boston@gmail.com", "Bird Watcher", "There's a bird in the yard! ")
            if label == "red bird":
                if len(os.listdir("red_bird")) < 20:
                    cv2.imwrite(f"red_bird/redbird_{datetime.now()}.jpg", frame)
                    send_email("lopamudra.boston@gmail.com", "Bird Watcher", "There's a bird in the yard! ")
            if label == "black bird":
                if len(os.listdir("black_bird")) < 20:
                    cv2.imwrite(f"black_bird/blackbird_{datetime.now()}.jpg", frame)
                    send_email("lopamudra.boston@gmail.com", "Bird Watcher", "There's a bird in the yard! ")
        annotated_frame = result.plot(boxes=True, masks=False)
        cv2.imshow("Camera", annotated_frame)
        if cv2.waitKey(1) == ord("q"):
            break


cv2.destroyAllWindows()
