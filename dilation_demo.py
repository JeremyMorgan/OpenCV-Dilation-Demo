# import the necessary libraries
import cv2
import numpy as np

# read in the image as grayscale using OpenCV's imread() function
image = cv2.imread('images/mustang.png', cv2.IMREAD_GRAYSCALE)

# create a 5x5 kernel of ones using NumPy's ones() method
# the datatype is set to unsigned 8-bit integer
kernel = np.ones((5, 5), np.uint8)

# dilate the image using the kernel with 2 iterations
# dilation is a morphological operation that expands the boundaries of objects in an image
dilated_image = cv2.dilate(image, kernel, iterations=2)

# display the original and dilated images using OpenCV's imshow() function
# the window names are provided as the first argument
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', dilated_image)

# wait for a key press before closing the windows
# the argument passed to waitKey() specifies the delay in milliseconds
# a value of 0 means the window will stay open indefinitely until a key is pressed
cv2.waitKey(0)

# clean up by destroying all the windows
cv2.destroyAllWindows()
