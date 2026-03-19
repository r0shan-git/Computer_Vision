import cv2

image=cv2.imread("1.Phase/rg.png")

if image is not None:
    sucess=cv2.imwrite("Output_python.png",image)
    if sucess:
        print("Image saved sucessfully as 'Output_python.png'")
    else:
        print("Failed to save an image")

else:
    print("Error : Could not load image")