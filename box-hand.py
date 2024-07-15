import cv2
import mediapipe as mp
import time
from tabulate import tabulate
import os

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands 
hands = mpHands.Hands() 
mpDraw = mp.solutions.drawing_utils 

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
                cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)

        os.system('clear') 
        print(tabulate(table_data, headers=["ID", "X", "Y"], tablefmt="grid"))

    cv2.imshow("Basic Hand Skeleton", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 