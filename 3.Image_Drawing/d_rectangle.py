import cv2

image=cv2.imread("3.phase/rg.png")

if image is None:
    print("Could not load the image ")
else:
    pt1=(100,100)
    pt2=(500,500)

    color=(0,0,255)

    thickness=3

    cv2.rectangle(image,pt1,pt2,color,thickness)

    cv2.imshow("Image foucussing rectangle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()