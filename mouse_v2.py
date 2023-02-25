import pyautogui
import cv2
from cvzone.HandTrackingModule import HandDetector
import time

pyautogui.FAILSAFE = False

def VirtualMouseV2(camNum = 0):
    
    try:
        screenWidth, screenHeight = pyautogui.size()
        winname = "Youth HCMUTE"
        cap = cv2.VideoCapture(camNum, cv2.CAP_DSHOW)
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
            # hands = detector.findHands(img, flipType=False, draw=False)
            hands, img = detector.findHands(img, flipType=False, draw=True)

            if hands:
                lmList = hands[0]['lmList']
                # Get the tip of the index finger
                x, y = lmList[8][:2]
                scale = screenWidth / img.shape[1]
                x_, y_ = x*scale, y*scale
                
                cv2.circle(img, (x, y), 15, (255, 0, 255), cv2.FILLED)
                # Check which fingers are up
                fingers = detector.fingersUp(hands[0])
                # Index finger up
                if fingers[1] == 1:
                    pyautogui.moveTo(x_, y_)
                # Othervise
                else:
                    pyautogui.click() # click left mouse button
                    time.sleep(1)
                
            # Display
            cv2.imshow(winname, img)
            cv2.waitKey(1)

    except:
        cv2.destroyAllWindows()
        cap.release()

if __name__ == "__main__":
    VirtualMouseV2()