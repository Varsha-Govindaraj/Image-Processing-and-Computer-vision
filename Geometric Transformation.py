import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
img = cv2.imread(r"C:\Users\Student\Downloads\cat.jpg")

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rows, cols = img.shape[:2]

# Translation
M_translate = np.float32([[1, 0, 50], [0, 1, 100]])
translated = cv2.warpAffine(img, M_translate, (cols, rows))

# Rotation
M_rotate = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated = cv2.warpAffine(img, M_rotate, (cols, rows))

# Scaling
scaled = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

# Affine Transformation
pts1 = np.float32([[50, 50], [200, 50], [50, 250]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M_affine = cv2.getAffineTransform(pts1, pts2)
affine = cv2.warpAffine(img, M_affine, (cols, rows))

# Display results
plt.subplot(231), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title("Original")
plt.subplot(232), plt.imshow(img_gray, cmap="gray"), plt.title("Gray")
plt.subplot(233), plt.imshow(cv2.cvtColor(translated, cv2.COLOR_BGR2RGB)), plt.title("Translated")
plt.subplot(234), plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)), plt.title("Rotated")
plt.subplot(235), plt.imshow(cv2.cvtColor(scaled, cv2.COLOR_BGR2RGB)), plt.title("Scaled")
plt.subplot(236), plt.imshow(cv2.cvtColor(affine, cv2.COLOR_BGR2RGB)), plt.title("Affine")
plt.show()