import cv2
import numpy as np

video=cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")

imp = input("Enter user id : ")
a=1
num = 1
while True:
    a=a+1
    check,frame=video.read()
    frame2 = frame

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=8)


    for x, y, w, h in faces:
        img=cv2.rectangle(frame2, (x, y), (x + w, y + h), (0,0,255), 3)
        cropped = gray[y:y+h, x:x+w]
        cv2.imwrite('dataset/user.' +str(imp)+ '.' + str(num) + '.jpg', cropped)
        num += 1
    cv2.imshow('Face', frame2)
    key = cv2.waitKey(1)

    if key == 27:
        break


video.release()

cv2.destroyAllWindows()