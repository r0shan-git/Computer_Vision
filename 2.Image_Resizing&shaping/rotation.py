import cv2

# Load image
image = cv2.imread("2.Phase/rg.png")

if image is None:
    print("❌ Could not load image")

else:
    (h, w) = image.shape[:2]

    # Find center
    center = (w // 2, h // 2)

    # Rotation matrix (90 degree)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)

    # Rotate image
    rotated = cv2.warpAffine(image, M, (w, h))

    # Show images
    cv2.imshow("Original", image)
    cv2.imshow("Rotated", rotated)

    # Wait and close
    cv2.waitKey(0)
    cv2.destroyAllWindows()