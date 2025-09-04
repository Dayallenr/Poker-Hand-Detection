from ultralytics import YOLO
import cv2 as cv
import math
import PokerHandClassification

webcam = cv.VideoCapture(0)

model = YOLO("PokerDetectionBest.pt")

while True:

    ret, frame = webcam.read()
    results = model(frame, stream=True)
    hand = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1, y1, x2, y2)
            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]
            cv.putText(frame, f"{label} {conf:.2f}", (max(0, x1), max(10, y1)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            if conf > 0.5:
                hand.append(label)

    hand = list(set(hand))
    print("Current hand: ", hand)
    if len(hand) <= 5:
        results = PokerHandClassification.findPokerHand(hand)
        cv.putText(frame, f"Your hand is {results}", (max(100, 100), max(100, 100)), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    cv.imshow("Webcam", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.destroyAllWindows()
