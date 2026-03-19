import cv2   # Import OpenCV library

# Open webcam (0 = default camera)
camera = cv2.VideoCapture(0)

# Get width of video frame from camera
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))

# Get height of video frame from camera
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define codec (video compression format)
# 'XVID' is commonly used for .avi files
codec = cv2.VideoWriter_fourcc(*'XVID')

# Create video writer object
# Parameters:
# filename → output video file
# codec → compression type
# 20 → frames per second (FPS)
# (width, height) → frame size
recorder = cv2.VideoWriter("my_video.avi", codec, 20, (frame_width, frame_height))

# Start infinite loop to capture frames continuously
while True:

    # Read frame from camera
    # success → True if frame captured
    # image → actual frame (image)
    success, image = camera.read()

    # If frame not captured, exit loop
    if not success:
        print("Could not read frame")
        break

    # Write frame into video file
    recorder.write(image)

    # Display live webcam feed in window
    cv2.imshow("Recording Live", image)

    # Wait for 1 millisecond and check if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Recording stopped by user")
        break

# Release camera (free resource)
camera.release()

# Release video writer (save file properly)
recorder.release()

# Close all OpenCV windows
cv2.destroyAllWindows()