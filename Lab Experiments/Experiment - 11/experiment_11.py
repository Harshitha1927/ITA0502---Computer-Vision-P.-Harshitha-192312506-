
import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\User\OneDrive\Desktop\Image_Processing\image.jpg")

if image is None:
    print("Image not found. Check the image path.")
else:
    rotated = cv2.rotate(image, cv2.ROTATE_180)

    plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
    plt.title("180 Degree Clockwise Rotation")
    plt.axis("off")
    plt.show()
