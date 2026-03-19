import cv2

image=cv2.imread("2.Phase/rg.png")

if image is None:
    print("Image not found")

else:
    print("Image loaded")

    resized=cv2.resize(image,(300,300))

    cv2.imshow("Original Image",image)
    cv2.imshow("Resized Image",resized)

    cv2.imwrite("resized_output.png",resized)