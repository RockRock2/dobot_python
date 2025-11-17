import cv2
import time
import numpy as np
import hand_tracking_module as htm
import math


pTime = 0
cTime = 0
cap = cv2.VideoCapture('/dev/video2')
detector = htm.handDetector(detectionCon=0.7)

cap.set (3, 640)
cap.set (4, 480)

while True:
  success, img = cap.read()
  img = detector.findHands(img)
  lmList = detector.findPosition(img)
  if len(lmList) != 0:
    # print(lmList[4], lmList[8])

    x1, y1 = lmList[4][1], lmList[4][2]
    x2, y2 = lmList[8][1], lmList[8][2]

    cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)
    cv2.circle(img, (x2,y2), 15, (255,0,255), cv2.FILLED)
    cv2.line(img, (x1,y1), (x2,y2), (255,0,0), 3)
    cx, cy = (x1 + x2) // 2, (y1+ y2) // 2

    length = math.hypot(x2-x1 , y2 - y1)
    print(length)

  cTime = time.time()
  fps = 1/(cTime-pTime)
  pTime = cTime
      
  cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3, (255,0,255), 3)

  cv2.imshow("Video", img)

  if cv2.waitKey(20) & 0xFF==ord('d'):
    break

cap.release()
cv2.destroyAllWindows()