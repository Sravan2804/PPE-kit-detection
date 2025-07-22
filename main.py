from ultralytics import YOLO
import cv2 as cv


model = YOLO("D:\Projects\OpenCV\PPE-kit-detection\YOLO-weights\yolov8l.pt")

classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone',
              'Safety Vest', 'machinery', 'vehicle']

cap = cv.VideoCapture(r"D:\Projects\OpenCV\PPE-kit-detection\Assets\ppe1.mp4")

