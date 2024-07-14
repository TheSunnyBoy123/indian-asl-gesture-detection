import cv2
import time



def image(): # Function to capture and return image
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        cap.release()
        return None
    ret, frame = cap.read()
    if not ret:
        cap.release()
        print("Error: Failed to capture image.")
        return None
    else:
        cap.release()
        return frame

cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)


# comment out the following lines to check camera input

# while True:
#     img = image()
#     if img is not None:
#         cv2.imshow("Camera", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# frame = image()
# cv2.imshow("Camera", frame)
# time.sleep(10)


# function show live camera feed
def camera_feed():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        cap.release()
        return None
    while True:
        ret, frame = cap.read()
        if not ret:
            cap.release()
            print("Error: Failed to capture image.")
            return None
        else:
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

camera_feed()