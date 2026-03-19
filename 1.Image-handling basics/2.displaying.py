import cv2

image=cv2.imread("1.Phase/rg.png")

if image is not None:
    cv2.imshow("Image showing",image) # open window
    cv2.waitKey(0)  # wait for a key
    cv2.destroyAllWindows()  # close the window

else:
    print("Could not load the image")

