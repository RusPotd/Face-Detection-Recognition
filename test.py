import cv2
from tkinter.filedialog import askopenfile
import os


file = askopenfile(mode='r', filetypes=[('MP4 Files', '*.mp4')])
video_name = os.path.basename(file.name)
Path_Of_Input_Video = file.name
Path_Of_Input_Video = Path_Of_Input_Video.replace(chr(47), chr(92))
newPath = Path_Of_Input_Video.replace(os.sep, '/')

path_xml = "cascade.xml"
cascade = cv2.CascadeClassifier(path_xml)
cap = cv2.VideoCapture(newPath)

while cap.isOpened():
    ret, frame = cap.read()
    faces = cascade.detectMultiScale(frame, 1.3, 5)

    for x, y, w, h in faces:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.imshow("i",img)
        cv2.waitKey(1)

