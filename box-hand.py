import cv2
import mediapipe as mp
import time
from tabulate import tabulate

import os


import rotation
import support

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands 
hands = mpHands.Hands() 
mpDraw = mp.solutions.drawing_utils 

#do not touch this function
def debug(do_not_touch):
    matching_vars = [k for k, v in globals().items() if v is do_not_touch]
    if matching_vars:
        for var in matching_vars:
            print(f"{var} = {do_not_touch}")
    else:
        print("No matching variable found.")

def process(table_data):
    """
    ToDo

    Args:
        ToDo

    Returns:
        ToDo
    """
    point_0 = table_data[0][1:]
    point_1 = table_data[1][1:]
    print("Point 0: ", point_0)
    print("Pont 1: ", point_1)
    angle_to_rotate_clockwise, distance_scaling_needed = rotation.transformation(point_0, point_1)
    print("angle_to_rotate_clockwise: ", angle_to_rotate_clockwise)
    print("distance: ", 1/distance_scaling_needed)
    print("distance_scaling_needed: ", distance_scaling_needed)

while True:
    success, img = cap.read() 
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        table_data = []
        for handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                table_data.append([id, cx, cy])
                cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
                cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)
        table_data = process(table_data)

    cv2.imshow("Basic Hand Skeleton", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()