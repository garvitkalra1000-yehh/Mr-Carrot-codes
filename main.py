# ------------------------------------------------------------
# Crop Disease Detection using Python
# ------------------------------------------------------------
# This program analyzes a leaf image to detect whether
# the plant is healthy or diseased based on color patterns.
# ------------------------------------------------------------

import cv2
import numpy as np

# Step 1: Load image
image = cv2.imread("leaf.jpg")

if image is None:
    print("Error: Image not found.")
    exit()

# Step 2: Convert to HSV (better for color detection)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Step 3: Define green color range (healthy leaf)
lower_green = np.array([25, 40, 40])
upper_green = np.array([90, 255, 255])

# Step 4: Create mask for green areas
green_mask = cv2.inRange(hsv, lower_green, upper_green)

# Step 5: Calculate percentage of green area
green_pixels = np.sum(green_mask > 0)
total_pixels = image.shape[0] * image.shape[1]

green_percentage = (green_pixels / total_pixels) * 100

print(f"Green Area Percentage: {green_percentage:.2f}%")

# Step 6: Decision logic
if green_percentage > 60:
    print("Prediction: Healthy Leaf 🌿")
elif green_percentage > 30:
    print("Prediction: Slight Disease Detected ⚠️")
else:
    print("Prediction: Diseased Leaf 🍂")

# Step 7: Show images
cv2.imshow("Original Image", image)
cv2.imshow("Green Mask", green_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()