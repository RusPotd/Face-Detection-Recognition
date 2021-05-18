import cv2,time
import numpy as np
import threading
#from PIL import Image, ImageTk
#import io
#import os, sys
from tkinter import*

def view_frame_video():
    num=1
    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    left_cascade = cv2.CascadeClassifier("lefteye.xml")
    right_cascade = cv2.CascadeClassifier("righteye.xml")
    mouth_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
    a = 1
    while True:
        a = a + 1
        check, frame = video.read()
        # print(check)
        # print(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
        mouth = mouth_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=8)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=8)
        # eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.25, minNeighbors=5)
        eyeleft = left_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=8)
        eyeright = right_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=8)

        for x, y, w, h in faces:
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cropped = frame[y:y + h, x:x + w]
            # cv2.imwrite('Cropped.jpg', cropped)
            resize = cv2.resize(cropped, (50, 50))
            cv2.imwrite('resize.png', resize)

            for ex, ey, ew, eh in eyeleft:
                cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                croppedleft = gray[ey:ey + eh, ex:ex + ew]
                cv2.imwrite('Croppedleft.png', croppedleft)

            # cv2.imshow('croppedleft', croppedleft)
            # k = cv2.waitKey(0) & 0xFF

            for e1x, e1y, e1w, e1h in eyeright:
                cv2.rectangle(frame, (e1x, e1y), (e1x + e1w, e1y + e1h), (0, 255, 0), 2)
                croppedr = gray[e1y:e1y + e1h, e1x:e1x + e1w]
                cv2.imwrite('croppedright.png', croppedr)

            for p, q, r, s in mouth:
                cv2.rectangle(frame, (p, q), (p + r, q + s), (0, 255, 0), 2)
                croppedmouth = gray[q:q + s, p:p + r]
                cv2.imwrite('croppedmouth.png', croppedmouth)

        cv2.imwrite('D://VideoLabel_2//frame'+str(num)+'.png',frame)
        path='D://VideoLabel_2//frame'+str(num)+'.png'
        pht = PhotoImage(file=path)
        # l=Label(root,text="Display_frame",width=500,height=400,image=pht)
        l.config(image=pht)
        l.image=pht
        num=num+1

        '''key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
        elif key == ord('s'):
            cv2.imwrite('Video.png', gray)
            cv2.destroyAllWindows()

        if key == ord('q'):
            break

    video.release()

    cv2.destroyAllWindows()'''
        if stop == True:
            video.release()
            break  # stop the loop thus stops updating the label and reading imag=e frames
        cv2.waitKey(1)
    video.release()


def stop():
    global stop
    stop = True


def play():
    stop = False
    t = threading.Thread(target=view_frame_video)
    t.start()
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

#Gives title to the window
root.title('Face_Recognition')
l=Label(root,bg="pink",bd=3)
l.pack(side=RIGHT,anchor=N,padx=200,pady=60)
#l.grid(row=1,column=30)

l2=Label(root,text="Enter URL")
entry=Entry(root)
l2.pack(side=LEFT,anchor=N,padx=10,pady=10)
entry.pack(side=LEFT,anchor=N,padx=10,pady=10)

b=Button(root,text="Play",command=play)
b.pack(side=LEFT,anchor=N,padx=40,pady=60)
#b.grid(padx=30,pady=60)

b2=Button(root,text="Stop",command=stop)
b2.pack(side=LEFT,anchor=N,padx=40,pady=60)

#l=Label(root,text="This is label")
#l.pack(side=LEFT)

root.mainloop()