import cv2

video=cv2.VideoCapture(0)

faceDetect=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

eyeDetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (350, 350))  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(frame, 1.3,5)
    for (x, y, w, h) in faces:
        x1,y1 = x + w, y + h
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 1)  # Draw rectangle around detected face
        cv2.putText(frame, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)  # Label the face
       
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eyeDetect.detectMultiScale(roi_gray, 1.1, 10)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            cv2.putText(roi_color, "Eye", (ex, ey - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
        cv2.line(frame, (x, y), (x+30,y), (255, 0, 255), 6) # Draw a line from the top-left corner
        cv2.line(frame, (x, y), (x,y+30), (255, 0, 255), 6)
        cv2.line(frame, (x1, y), (x1-30,y), (255, 0, 255), 6)
        cv2.line(frame, (x1, y), (x1,y+30), (255, 0, 255), 6)
        cv2.line(frame, (x, y1), (x+30,y1), (255, 0, 255), 6)
        cv2.line(frame, (x, y1), (x,y1-30), (255, 0, 255), 6)
        cv2.line(frame, (x1, y1), (x1-30,y1), (255, 0, 255), 6)
        cv2.line(frame, (x1, y1), (x1,y1-30), (255, 0, 255), 6)

    cv2.imshow('Video Feed', frame)
    k=cv2.waitKey(1)
    if k== ord('q'):  # Press 'q' to quit
        break
video.release()
cv2.destroyAllWindows()



