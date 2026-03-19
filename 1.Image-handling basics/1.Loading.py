import cv2
image =cv2.imread("1.Phase/ChatGPT Image Mar 5, 2026, 10_21_30 AM.png")
if image is None:
    print("Error Image not found")
else:
    print("Image Loaded sucessfully")