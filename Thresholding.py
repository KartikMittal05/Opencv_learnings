import cv2
img=cv2.resize(cv2.imread('SAVE_20210319_165944.jpg',0), (350, 350))  # Load and resize the image to 512x512


def onChange(val):
    pass

cv2.namedWindow('frame') 
cv2.createTrackbar("Thresholding", "frame", 0, 255, onChange)  

while True:
    cv2.imshow('frame', img)  # Display the original image

    val=cv2.getTrackbarPos("Thresholding", "frame")

    ret,threshold= cv2.threshold(img, val, 255, cv2.THRESH_BINARY)  # Apply binary thresholding
    ret_inv, threshold_inv = cv2.threshold(img, val, 255, cv2.THRESH_BINARY_INV)  # Apply inverse binary thresholding
    ret_trunc, threshold_trunc = cv2.threshold(img, val, 255, cv2.THRESH_TRUNC)  # Apply truncation thresholding
    ret_tozero, threshold_tozero = cv2.threshold(img, val, 255, cv2.THRESH_TOZERO)  # Apply to-zero thresholding
    ret_tozero_inv, threshold_tozero_inv = cv2.threshold(img, val, 255, cv2.THRESH_TOZERO_INV)  # Apply inverse to-zero thresholding

   
    cv2.imshow('Thresholding Binary', threshold)  # Display the binary thresholded image
    cv2.imshow('Thresholding Binary Inverse', threshold_inv)  # Display the inverse binary thresholded image
    cv2.imshow('Thresholding Trunc', threshold_trunc)  # Display the trunc
    cv2.imshow('Thresholding ToZero', threshold_tozero)  # Display the to-zero thresholded image
    cv2.imshow('Thresholding ToZero Inverse', threshold_tozero_inv) # Display the inverse to-zero thresholded image

    k=cv2.waitKey(1) 
    if k== ord('q'):
        break
cv2.destroyAllWindows()  