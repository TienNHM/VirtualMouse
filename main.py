import autopy
import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import numpy as np

##########################
wCam, hCam = 1920, 1080
frameR = 0 # Frame Reduction
smoothening = 2
#########################
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
wScr, hScr = autopy.screen.size()

detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    # img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False, )

    if hands:
        lmList = hands[0]['lmList']

        # 2. Get the tip of the index and middle fingers
        x1, y1 = lmList[8][:2]
        x2, y2 = lmList[12][:2]

        # 3. Check which fingers are up
        fingers = detector.fingersUp(hands[0])
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

        # 4. All fingers up
        if fingers[1] == 1:
            # 5. Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            # 6. Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            # 7. Move Mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY
            
            

        # 8. All fingers down
        if fingers[1] == 0:
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            autopy.mouse.click()
            print("Clicked!")
            time.sleep(0.5)
        
    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)