import numpy as np
import cv2, os
from PIL import Image

rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recogniser/trainingData.yml")
#font = cv2.InitFont(cv2.CV_FONT_HERSHEY_COMPLEX_SMALL, 5, 1,0,4)
font = cv2.FONT_HERSHEY_SIMPLEX
video=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=8)
    for x, y, w, h in faces:
        img=cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,255), 3)
        cropped = gray[y:y+h, x:x+w]
        id, conf = rec.predict(cropped)
        if id == 1:
            id = "Rushikesh"
        elif id == 2:
            id = "Barack Obama"
        elif id == 3:
            id = "Ashitosh"
        elif id == 4:
            id = "Ashish"
        elif id == 5:
            id = "kajol"

        else:
            id = "Other"
        cv2.putText(frame, str(id)+str(conf), (x, y+h+40), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("Faces", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()

cv2.destroyAllWindows()


