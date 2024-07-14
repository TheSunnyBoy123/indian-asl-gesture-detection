import cv2
import numpy as np
import time

def image(): 
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

while True:
    # Capture image
    img = image()
    # If image is captured
    if img is not None:
        # detect hand using the module cv2.CascadeClassifier
        hand_cascade = cv2.CascadeClassifier('hand.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hands = hand_cascade.detectMultiScale(gray, 1.1, 5)
        # Draw a box around the hand
        for (x, y, w, h) in hands:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display the image
        cv2.imshow("Camera", img)
