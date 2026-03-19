import cv2

image=cv2.imread("1.Phase/rg.png")

if image is not None:
    # image dimension (height,width,color channel)
    h,w,c=image.shape
    print(f"Image loaded:\n {h}\n Width :{w}\n Channels:{c}")

else:
    print("Could not load image")