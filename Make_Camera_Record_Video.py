import cv2

video=cv2.VideoCapture(0)  # Initialize the camera for video capture

# print(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # Print the width of the video frame
# print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Print the height of the video                    

# video.set(3,300)  # Set the width of the video frame
# video.set(4,300)  # Set the height of the video frame

fource=cv2.VideoWriter_fourcc(*'MPEG')  # Define the codec for video writing
out=cv2.VideoWriter('output.avi', fource, 30.0, (500, 500))  # Create a VideoWriter object

while True:
    ret, frame=video.read()  # Read a frame from the camera
    out.write(frame)  # Write the frame to the output video file
    if not ret:
        break  # If no frame is captured, exit the loop

    cv2.imshow('Video', frame)  # Display the captured frame in a window

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit if 'q' is pressed
        break
video.release()  # Release the camera
out.release()  # Release the VideoWriter object
cv2.destroyAllWindows()  # Close all OpenCV windows