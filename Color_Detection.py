import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image 
img = cv2.imread("C:\\Users\\Acer\\Desktop\\Project 16\\hill.jpeg")

# Convert image from BGR to RGB 
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert image from RGB to HSV color space
img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

# Define the upper and lower bounds for the HSV values 
lower = np.array([25,150,50])
upper = np.array([75,255,255])

# Create a mask that identifies pixels 
mask = cv2.inRange(img_hsv, lower, upper)

# Apply the mask to RGB image 
res = cv2.bitwise_and(img_rgb,img_rgb, mask=mask)

# Create a figure to display original and processed image side by side
plt.figure(figsize=(15,5))

# For original image
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.axis('off')
plt.title("Original Image")

# For processed image
plt.subplot(1,2,2)
plt.imshow(res)
plt.axis('off')
plt.title("Highlighting Green Color")

# Display both images
plt.show()