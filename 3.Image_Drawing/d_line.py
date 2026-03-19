import cv2

# image=cv2.imread("3.phase/rg1.jpg")
image=cv2.imread("3.phase/rg.png")

if image is None:
    print("Could not load Image")

else:
    # Draw the line 
    pt1=(50,100)
    pt2=(300,100)

    color=(250,0,0)
    thickness=4

    cv2.line(image,pt1,pt2,color,thickness)

    cv2.imshow("Line Drawing ",image)
    cv2.waitKey(0)
    cv2.destoryAllWindows()

