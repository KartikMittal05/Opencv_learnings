import cv2

video = cv2.VideoCapture(0)

def onChange(val):
    print("Value Count")  # Callback function for trackbar changes

cv2.namedWindow('frame')  # Create a window to display the video frame
cv2.createTrackbar("test", "frame", 0, 2, onChange)  # Create a trackbar
cv2.createTrackbar("rect", "frame", 50, 255, onChange)


while True:
    ret, frame = video.read()
    val=cv2.getTrackbarPos("test", "frame")  # Get the current position of the trackbar
    rect1=cv2.getTrackbarPos("rect", "frame")
    cv2.rectangle(frame, (0, 0), (rect1, rect1), (50, 50, 255), -4)
    cv2.putText(frame, str(val), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (50,50, 255),3)  # Display the trackbar value on the frame
    if val == 0:
        pass
    elif val == 1:
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
    elif val == 2:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
