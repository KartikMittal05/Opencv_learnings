import cv2
img=cv2.imread('SAVE_20210319_165944.jpg',flags=0) # Load the image in grayscale(flags=0)

print(img)  # Print the shape of the image

cv2.imshow('image', img)  # Display the image in a window

cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows

cv2.imwrite('gray_image.jpg', img)  # Save the image to a file