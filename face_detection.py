import cv2
import os
import numpy as np

def faceDetection(test_img):
    gray_img = cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('C:\\Users\\Ashutosh\\Pictures\\opencv-master\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=5)

    return faces,gray_img

def labels_for_training_data(directory):
    faces = []
    faceID = []

    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):            #ignoring .git types of files
                print("Skipping system files....")
                continue

            id = os.path.basename(path)             #Label
            img_path = os.path.join(path,filename)  #image path
            print("Img_path : ",img_path)
            print("id : ",id)
            test_img = cv2.imread(img_path)
            if test_img is None:
                print("Image not loaded properly..")
                continue
            faces_rect,gray_img = faceDetection(test_img)
            if len(faces_rect)!=1:
                continue        #We are assuming only single person images are being fed to classifier
            (x,y,w,h) = faces_rect[0]
            #roi - region of interest
            roi_gray = gray_img[y:y+w,x:x+h]        #cropping face part from the whole image
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces,faceID

def train_classifier(faces,faceID):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()  #Local Binary Pattern Histogram
    face_recognizer.train(faces,np.array(faceID))
    return face_recognizer

def draw_rect(test_img,face):
    (x,y,w,h) = face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=3)

def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),1)