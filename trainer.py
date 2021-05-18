import numpy as np
import cv2, os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "dataset"

def getImagesWithId(path):
    imagepaths = [os.path.join(path, f) for f in os.listdir(path)]
    Faces = []
    IDs = []
    for imagepath in imagepaths:
        img = cv2.imread(imagepath , 0)
        ID = int(os.path.split(imagepath)[-1].split('.')[1])
        Faces.append(img)
        IDs.append(ID)

    return np.array(IDs) , Faces

IDs, Faces = getImagesWithId(path)
recognizer.train(Faces, IDs)

recognizer.save("recogniser/trainingData.yml")
cv2.destroyAllWindows()
