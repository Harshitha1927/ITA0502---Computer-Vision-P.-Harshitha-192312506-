
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

dilated = cv2.dilate(image, kernel, iterations=1)

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(dilated, cv2.COLOR_BGR2RGB))
plt.title("Dilated Image")

plt.show()
