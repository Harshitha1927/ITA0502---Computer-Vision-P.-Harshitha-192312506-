
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")

bigger = cv2.resize(image, None, fx=2, fy=2)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5)

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB))
plt.title("Bigger Image")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB))
plt.title("Smaller Image")

plt.show()
