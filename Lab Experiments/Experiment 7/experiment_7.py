
import cv2
import os

print("Current folder:", os.getcwd())

cap = cv2.VideoCapture("video.mp4")

print("Video opened:", cap.isOpened())

ret, frame = cap.read()
print("Frame read:", ret)

if ret:
    cv2.imshow("My Video Output", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Video not found or cannot be read!")

cap.release()
