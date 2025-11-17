import cv2
import time
import numpy as np
import hand_tracking_module as htm
import math
import os

# folderPath = "pic_paint"
# myList = os.listdir(folderPath)
# print(myList)
# overlayList = []

img2 = cv2.imread("handtracking/pxfuel.jpg")

# cv2.imshow("ori", img2)

cropped_img2 = img2[365:490 , 0:1280]

# cv2.imshow("cropped", cropped_img2)

pTime = 0
cTime = 0
cap = cv2.VideoCapture('/dev/video2')
detector = htm.handDetector(detectionCon=0.7)

cap.set (3, 1280)
cap.set (4, 720)

while True:
  success, img = cap.read()

  # 2. Find Hand
  img = detector.findHands(img)
  lmList = detector.findPosition(img, draw=False)

  if len(lmList) != 0:
    print(lmList)

  # 3. Check finger

  # 4. Check if touching 

  # 5. move robot


  img[0:125 , 0:1280] = cropped_img2

  cTime = time.time()
  fps = 1/(cTime-pTime)
  pTime = cTime
      
  cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3, (255,0,255), 3)

  cv2.imshow("Video", img)

  if cv2.waitKey(20) & 0xFF==ord('d'):
    break

cap.release()
cv2.destroyAllWindows()