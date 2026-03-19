import cv2

img=cv2.imread("5.Edge_deactionandTresholding/man.png",cv2.IMREAD_GRAYSCALE)

ret,thresh_img=cv2.threshold(img,120,255,cv2.THRESH_BINARY)





cv2.imshow("Original Image",img)
cv2.imshow("Edges",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()