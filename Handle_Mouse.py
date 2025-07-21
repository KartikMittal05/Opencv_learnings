import cv2

def mouse_draw_catch(event, x, y,flags, params):
    if event == cv2.EVENT_MOUSEMOVE:
        circles.append((x, y))  # Store the position of the mouse click
        cv2.circle(frame, (x, y), 60, (50,50,255), 2) # Draw a circle at the mouse click position
    # if event == cv2.EVENT_MOUSEMOVE:
    #     print("Mouse Move")
    # elif event == cv2.EVENT_LBUTTONDOWN:
    #     print("Mouse Left Button Clicked")
    # elif event == cv2.EVENT_RBUTTONDOWN:
    #     print("Mouse Right Button Clicked")
    # elif event == cv2.EVENT_LBUTTONDBLCLK:
    #     print("Mouse Left Button Double Clicked")

video=cv2.VideoCapture(0)
circles=[]  # List to store the positions of mouse clicks

cv2.namedWindow('frame')  # Create a window to display the video frame
cv2.setMouseCallback('frame', mouse_draw_catch)  # Set a mouse callback function

while True:
    ret,frame=video.read()
    for pos in circles:
        cv2.circle(frame, pos, 3, (50,50,255), -1)  # Draw circles at the stored positions
    cv2.imshow('frame', frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
    elif k==ord('c'):
        circles.pop(0)  # Remove the first circle from the list
    elif k==ord('d'):
        circles=[]
video.release()
cv2.destroyAllWindows()