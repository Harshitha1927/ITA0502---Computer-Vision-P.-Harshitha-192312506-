
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("image.jpg")
rows, cols = image.shape[:2]

points1 = np.float32([[50, 50], [200, 50], [50, 200]])
points2 = np.float32([[10, 100], [200, 50], [100, 250]])

matrix = cv2.getAffineTransform(points1, points2)
transformed = cv2.warpAffine(image, matrix, (cols, rows))

plt.imshow(cv2.cvtColor(transformed, cv2.COLOR_BGR2RGB))
plt.title("Affine Transformation")
plt.show()
