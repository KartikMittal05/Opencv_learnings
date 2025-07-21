import cv2
import numpy as np


img=np.zeros((512, 512,3), dtype=np.uint8)

cv2.line(img, (0, 20), (200, 20), (255, 0, 0), 5)  # Draw a blue diagonal line
cv2.line(img, (0, 40), (200, 40), (255, 0, 0), 5) 
cv2.line(img, (0, 60), (200, 60), (255, 0, 0), 5) 

cv2.arrowedLine(img, (0, 80), (200, 80), (255, 0, 0), 5)  # Draw a blue arrowed line


cv2.circle(img, (100, 100), 50, (0, 255, 0), -1)  # Draw a filled green circle

cv2.rectangle(img, (50, 150), (200, 300), (0, 0, 255), 3)  # Draw a red rectangle

cv2.putText(img, 'OpenCV', (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)  # Add white text


cv2.imshow('image', img) 

cv2.waitKey(0) 
cv2.destroyAllWindows()  