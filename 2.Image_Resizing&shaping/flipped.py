import cv2

image=cv2.imread("2.Phase/rg.png")

if image is None:
    print("Could not load image")

else:
    flipped_horizontal=cv2.flip(image,1)
    flipped_vetical=cv2.flip(image,0)
    flipped_both=cv2.flip(image,-1)

    cv2.imshow("Original",image)
    cv2.imshow("Flipped Horizontal",flipped_horizontal)
    cv2.imshow("Flipped vertical",flipped_vetical)
    cv2.imshow("Flipped Both",flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()