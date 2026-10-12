
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
gray = gray.astype("float32")

corners = cv2.cornerHarris(gray, 2, 3, 0.04)
image[corners > 0.01 * corners.max()] = [0, 0, 255]

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Harris Corner Detection")
plt.show()
