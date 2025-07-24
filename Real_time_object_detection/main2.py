from ultralytics import YOLO
import cv2
import math

# Load video file instead of webcam
cap = cv2.VideoCapture('C:/Users/91902/Desktop/Opencv2/Real_time_object_detection/3175-166339863_small.mp4')


# Load YOLOv8 model
model = YOLO('../YOLO Weights/yolov8n.pt')

# COCO Class labels
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train",
              "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter",
              "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear",
              "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase",
              "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle",
              "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
              "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut",
              "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet",
              "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave",
              "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

# Main loop
while True:
    success, img = cap.read()
    if not success:
        print("End of video or cannot read the file.")
        break

    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding box
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            w, h = x2 - x1, y2 - y1

            # Draw rectangle
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100

            # Class label
            cls = int(box.cls[0])
            name = classNames[cls]
            label = f"{name} {conf}"

            # Label background
            (text_width, text_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
            cv2.rectangle(img, (x1, y1 - 20), (x1 + text_width, y1), (255, 0, 255), -1)

            # Draw text
            cv2.putText(img, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    cv2.imshow("YOLOv8 Video Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
