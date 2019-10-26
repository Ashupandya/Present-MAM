import cv2
import os
import numpy as np
import face_recognition as fr
import face_detection as fd
from xlwt import Workbook, Formula, easyxf
import xlwriter as xl
from datetime import datetime as dt
lab = []
fac = []
n = input("Enter Teacher's name : ")

test_img = cv2.imread('C:\\Users\\Ashutosh\\Documents\\PycharmProjects\\test_images_Major\\images (11).jpg')
faces_detected,gray_img = fd.faceDetection(test_img)
print("Face detected: ",faces_detected)

#extra

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('C:\\Users\\Ashutosh\\Documents\\PycharmProjects\\Major\\venv\\training_Data.yml')
name = {0:"Obama",1:"Trump"}
number = 0
count = 0
for _ in faces_detected:
    number = number+1
    count = count+1

for face in faces_detected:
    (x,y,w,h) = face
    roi_gray = gray_img[y:y+h,x:x+h]
    labels,confidence = face_recognizer.predict(roi_gray)
    print("Confidence : ",confidence)
    print("Labels : ",labels)
    lab.append(labels)
    fd.draw_rect(test_img,face)
    predicted_name = name[labels]
    fac.append(predicted_name)
    fd.put_text(test_img,predicted_name,x,y)

xl.xlt(n,number,lab,fac)


resized_img = cv2.resize(test_img,(400,400))
cv2.imshow("Face detection practice",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()