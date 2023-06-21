import cv2

# Using the cascade that I have downloaded
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Using a Webcam or linking the video file

webcam = cv2.VideoCapture('videoplayback.mp4')

# iteration
while True:

    # Reading a frame
    successful_frame_read, frame = webcam.read()

    # Grayscale is the only filter my algorithm knows
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # COORDINATES
    coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # rectangles
    for (x, y, h, w) in coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (256, 0, 0), 2)
    cv2.imshow('Facecam', frame)
    key = cv2.waitKey(1)
    # Ascii value of q/Q is given to stop the program
    if key == 81 or key == 113:
        break
# webcam.release()