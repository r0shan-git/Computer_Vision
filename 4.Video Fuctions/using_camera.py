import cv2

camera=cv2.VideoCapture(0)

while True:
    ret,frame=camera.read() # ret=True/false frame=image

    if not ret:
        print("Could not read frame")
        break
    cv2.imshow("Webcam feed",frame)


    if cv2.waitKey(1) &0xFF==ord('q'):
        print("Quitting.....")

        break

camera.release()
cv2.destroyAllWindows()