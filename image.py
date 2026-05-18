import cv2
import numpy as np
import os

# Create output folder
if not os.path.exists("output"):
    os.makedirs("output")

# -----------------------------
# 1. Read and Display Image
# -----------------------------
image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found!")
    exit()

cv2.imshow("Original Image", image)

# -----------------------------
# 2. Save Original Image
# -----------------------------
cv2.imwrite("output/original_saved.jpg", image)

# -----------------------------
# 3. Resize Image
# -----------------------------
resized = cv2.resize(image, (400, 300))
cv2.imshow("Resized Image", resized)
cv2.imwrite("output/resized.jpg", resized)

# -----------------------------
# 4. Rotate Image
# -----------------------------
height, width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)

rotated = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow("Rotated Image", rotated)
cv2.imwrite("output/rotated.jpg", rotated)

# -----------------------------
# 5. Flip Image
# -----------------------------
flipped = cv2.flip(image, 1)

cv2.imshow("Flipped Image", flipped)
cv2.imwrite("output/flipped.jpg", flipped)

# -----------------------------
# 6. Crop Image
# -----------------------------
cropped = image[50:300, 100:400]

cv2.imshow("Cropped Image", cropped)
cv2.imwrite("output/cropped.jpg", cropped)

# -----------------------------
# 7. NumPy Array Operations
# -----------------------------
print("Image Shape:", image.shape)
print("Image Size:", image.size)
print("Image Data Type:", image.dtype)

# Create a black image using NumPy
black_image = np.zeros((300, 300, 3), dtype=np.uint8)

cv2.imshow("Black Image", black_image)

# -----------------------------
# 8. Split Color Channels
# -----------------------------
blue, green, red = cv2.split(image)

cv2.imshow("Blue Channel", blue)
cv2.imshow("Green Channel", green)
cv2.imshow("Red Channel", red)

# -----------------------------
# 9. Merge Color Channels
# -----------------------------
merged = cv2.merge((blue, green, red))

cv2.imshow("Merged Image", merged)
cv2.imwrite("output/merged.jpg", merged)

# -----------------------------
# Wait and Close
# -----------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()