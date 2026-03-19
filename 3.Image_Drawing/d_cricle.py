import cv2

image=cv2.imread("3.phase/rg.png")

if image is None:
    print("Image is not loaded")

else:
    print("Image loaded sucessfully")

    #(img,center,radius,color,thickness)

    cv2.circle(image,(250,250),100,(255,0,0),5)

    cv2.imshow("Drawing Circle",image)
    cv2.waitKey(0)
    cv2.destoryAllWindows()