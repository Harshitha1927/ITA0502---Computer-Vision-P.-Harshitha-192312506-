
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")

rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
plt.title("270 Degree Clockwise Rotation")
plt.show()
