import cv2
import mediapipe as mp
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]

wCam, hCam = 640, 480
detection_confidence = 0.5
tracking_confidence = 0.5
model_complexity = 0 
min_length = 50  
max_length = 220 
volBarMax = 400  
volBarMin = 150  

circle_color_active = (0, 255, 0)  
circle_color_inactive = (0, 0, 255)  
circle_color_thumb = (255, 255, 255) 
circle_color_index = (255, 255, 255) 
line_thickness = 3


cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)


with mp_hands.Hands(
    model_complexity=model_complexity,
    min_detection_confidence=detection_confidence,
    min_tracking_confidence=tracking_confidence) as hands:

    while cam.isOpened():
        success, image = cam.read()


        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

            myHand = results.multi_hand_landmarks[0]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

        if len(lmList) != 0:
            x1, y1 = lmList[4][1], lmList[4][2]  # Thumb
            x2, y2 = lmList[8][1], lmList[8][2]  # Index

            cv2.circle(image, (x1, y1), 15, circle_color_thumb, cv2.FILLED)
            cv2.circle(image, (x2, y2), 15, circle_color_index, cv2.FILLED)
            cv2.line(image, (x1, y1), (x2, y2), circle_color_active, line_thickness)

            # Calculate length between thumb and index
            length = math.hypot(x2 - x1, y2 - y1)


            if length < min_length:
                cv2.line(image, (x1, y1), (x2, y2), circle_color_inactive, line_thickness)

            vol = np.interp(length, [min_length, max_length], [minVol, maxVol])
            volume.SetMasterVolumeLevel(vol, None)


            volBar = np.interp(length, [min_length, max_length], [volBarMax, volBarMin])
            volPer = np.interp(length, [min_length, max_length], [0, 100])

            cv2.rectangle(image, (50, volBarMin), (85, volBarMax), (0, 0, 0), 3)
            cv2.rectangle(image, (50, int(volBar)), (85, volBarMax), (0, 0, 0), cv2.FILLED)
            cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

        cv2.imshow('Hand Detector', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()
