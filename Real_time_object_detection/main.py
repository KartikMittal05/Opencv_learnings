import cv2
from ultralytics import YOLO
import random

# Load YOLO model
yolo = YOLO('yolov5s.pt')

# Open webcam
videoCap = cv2.VideoCapture('C:/Users/91902/Desktop/Opencv2/Real_time_object_detection/3175-166339863_small.mp4')


# Set higher resolution
videoCap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
videoCap.set(cv2.CAP_PROP_FRAME_HEIGHT,1280)


# Function to get unique colors

# Fixed bright colors (BGR format for OpenCV)
color_palette = [
    (255, 0, 0),    # Blue
    (0, 0, 255),    # Red
    (0, 255, 255),  # Yellow
    (0, 255, 0),    # Green
    (255, 0, 255),  # Magenta (optional fallback)
    (255, 255, 0),  # Cyan (optional fallback)
]
def getColours(cls_num):
    return color_palette[cls_num % len(color_palette)]

# def getColours(cls_num):
#     random.seed(cls_num)
#     return tuple(random.randint(128, 255) for _ in range(3))

while True:
    ret, frame = videoCap.read()
    if not ret:
        continue

    results = yolo.track(frame, stream=True)

    for result in results:
        if result.boxes is not None:
            classes_names = result.names

            for box in result.boxes:
                if box.conf.item() > 0.4:
                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                    cls = int(box.cls.item())
                    class_name = classes_names[cls]
                    colour = getColours(cls)

                    cv2.rectangle(frame, (x1, y1), (x2, y2), colour, 2)
                    cv2.putText(frame, f'{class_name} {box.conf.item():.2f}', 
                                (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                                0.9, colour, 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCap.release()
cv2.destroyAllWindows()
