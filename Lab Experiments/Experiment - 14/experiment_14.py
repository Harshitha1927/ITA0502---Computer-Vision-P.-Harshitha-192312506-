
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("image.jpg")
rows, cols = image.shape[:2]

points1 = np.float32([[0, 0], [cols-1, 0],
                      [0, rows-1], [cols-1, rows-1]])

points2 = np.float32([[50, 50], [cols-50, 0],
                      [0, rows-50], [cols-1, rows-1]])

matrix = cv2.getPerspectiveTransform(points1, points2)
transformed = cv2.warpPerspective(image, matrix, (cols, rows))

plt.imshow(cv2.cvtColor(transformed, cv2.COLOR_BGR2RGB))
plt.title("Perspective Transformation")
plt.show()
