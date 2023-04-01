# import the necessary libraries
import cv2  # library for computer vision tasks
import numpy as np  # library for numerical operations
import matplotlib.pyplot as plt  # library for visualization

# read in the image as grayscale using OpenCV's imread() function
image = cv2.imread('images/mustang.png', cv2.IMREAD_GRAYSCALE)

# create a 5x5 kernel of ones using NumPy's ones() method
# the datatype is set to unsigned 8-bit integer
kernel = np.ones((5, 5), np.uint8)

# dilate the image using the kernel with 2 iterations
# dilation is a morphological operation that expands the boundaries of objects in an image
dilated_image = cv2.dilate(image, kernel, iterations=2)

# create a figure with two subplots to show the original and dilated images side by side
plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(dilated_image,
                             cmap='gray'), plt.title('Dilated Image')
plt.show()
