from ultralytics import YOLO
import cv2 as cv
import cvzone
import math

model = YOLO(r"D:\Projects\OpenCV\PPE-kit-detection\best.pt")

classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']

#cap = cv.VideoCapture(r"D:\Projects\OpenCV\PPE-kit-detection\Assets\ppe2.mp4")

cap = cv.VideoCapture(0)


while True:
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1

            conf = math.ceil((box.conf[0] * 100)) / 100
            
            cls = int(box.cls[0])
            currentClass = classNames[cls]
            if conf > 0.5:
                if currentClass in ['NO-Hardhat', 'NO-Mask', 'NO-Safety Vest']:
                    myColor = (0, 0, 255)
                elif currentClass in ['Hardhat', 'Mask', 'Safety Vest']:
                    myColor = (0, 255, 0)
                else: 
                    myColor = (255, 0, 0)   

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1.5, thickness=2,colorB=myColor,
                                   colorT=(255,255,255),colorR=myColor, offset=7)
            cv.rectangle(img, (x1, y1), (x2, y2), myColor, 2)  
          
    cv.imshow("Image", img)
    cv.waitKey(1)
