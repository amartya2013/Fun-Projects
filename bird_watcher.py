import cv2
from ultralytics import YOLO
from datetime import datetime
import os
from emailer import send_email
from ai_response import get_response
import threading


print("Loading YOLO model...")
model = YOLO("yoloe-11s-seg.onnx")
print("Done Loading Model")



names = ["blue bird", "black bird", "red bird"]

for name in names:
    if not os.path.exists(name.replace(" ", "_")):
        os.mkdir(name.replace(" ", "_"))


# model.set_classes(names, model.get_text_pe(names))
capture = cv2.VideoCapture(0)

def process_bird(image_path):
    response = get_response("Tell me about the bird that is in the image?", image_path)
    send_email(
        "lopamudra.boston@gmail.com",
        "Bird Watcher",
        f"There's a bird in the yard! \n\n {response}",
    )

while True:
    ret, frame = capture.read()
    if ret:
        results = model.predict(frame)
        result = results[0]

        for box in result.boxes:
            class_id = int(box.cls[0])  # numeric class (e.g., 0, 1, 2)
            label = result.names[class_id]  # human-readable label (e.g., "person")

            if label:
                if len(os.listdir(f"{label.replace(" ", "_")}")) < 200:
                    name = f"{label.replace(" ", "_")}/{label.replace(" ", "")}_{datetime.now()}.jpg"
                    cv2.imwrite(name, frame)
                    process_bird(name)

        annotated_frame = result.plot(boxes=True, masks=False)
        cv2.imshow("Camera", annotated_frame)
        if cv2.waitKey(1) == ord("q"):
            break


cv2.destroyAllWindows()
