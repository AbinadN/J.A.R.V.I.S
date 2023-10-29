import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=1)
mySerial = SerialObject("COM3",9600, 1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=True)
    if hands:
        hand1 = hands[0]
        fingers1 = detector.fingersUp(hand1)
        print(f'Fingers Up: {fingers1}')
        mySerial.sendData(fingers1)

    cv2.imshow('Reflection', img)
    cv2.waitKey(1)
