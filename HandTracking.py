from cvzone.HandTrackingModule import HandDetector
import cv2
import serial

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7, maxHands=1)
mySerial = serial.Serial('COM3', 9600)

while True:
    success, img = cap.read()
    hand, img = detector.findHands(img)

    if hand:
        hand1 = hand[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1["center"]
        handType = hand1["type"]

        fingers = detector.fingersUp(hand1)
        print(fingers)
        mySerial.write(str(fingers).encode())

    cv2.imshow("image", img)
    cv2.waitKey(1)
