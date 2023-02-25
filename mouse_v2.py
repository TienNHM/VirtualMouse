import pyautogui
import cv2
from cvzone.HandTrackingModule import HandDetector
import time

pyautogui.FAILSAFE = False

def VirtualMouseV2():
    
    screenWidth, screenHeight = pyautogui.size()
    winname = "Youth HCMUTE"
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, screenWidth)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, screenHeight)
    # cv2.namedWindow(winname, cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty(winname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    detector = HandDetector(detectionCon=0.8, maxHands=1)
    
    first = True
    while first or cv2.getWindowProperty(winname, 0) >= 0:
        
        first = False
        _, img = cap.read()
        img = cv2.flip(img, 1)
        hands = detector.findHands(img, flipType=False, draw=False)

        if hands:
            lmList = hands[0]['lmList']
            # 2. Get the tip of the index finger
            x, y = lmList[8][:2]
            scale = screenWidth / img.shape[1]
            x_, y_ = x*scale, y*scale
            
            cv2.circle(img, (x, y), 15, (255, 0, 255), cv2.FILLED)
            # 3. Check which fingers are up
            fingers = detector.fingersUp(hands[0])
            # 4. All fingers up
            if fingers[1] == 1:
                pyautogui.moveTo(x_, y_)
            # 8. All fingers down
            else:
                pyautogui.click() # click left mouse button
                time.sleep(1)
            
        # 12. Display
        cv2.imshow(winname, img)
        cv2.waitKey(1)

if __name__ == "__main__":
    VirtualMouseV2()