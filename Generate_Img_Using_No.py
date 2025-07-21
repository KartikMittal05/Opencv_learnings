import cv2
import numpy as np

# img=cv2.imread('SAVE_20210319_165944.jpg',1) # Load the image in grayscale(flags=0)

img=np.zeros((512, 512, 3), dtype=np.uint8)  # Create a black image of size 512x512 with 3 color channels

# print(img.shape)  # Print the shape of the image
# print(img.dtype)  # Print the data type of the image
# print(type(img))  # Print the type of the image
# print(img.ndim)  # Print the number of dimensions of the image
# print(img.size)  # Print the total number of pixels in the image

cv2.imshow('image', img)  # Display the image in a window

cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows
