import cv2
import dlib
import numpy as np

# Loading landmarks detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/yigit/Documents/Git-Repos/ML-APIs/thirdparty/shape_predictor_68_face_landmarks.dat")
face_cascade = cv2.CascadeClassifier('/home/yigit/Documents/Git-Repos/ML-APIs/thirdparty/opencv/haarcascade_frontalface_default.xml')


def faceDetection(imFile):
    '''
    find faces and face landmarks on a given image
    @param imFile (str) : file name of the image
    @return : labeled image
    ''' 
    img = cv2.imread(imFile)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faceLandmarks = detector(gray)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for landmark in faceLandmarks:
        x1 = landmark.left()
        y1 = landmark.top()
        x2 = landmark.right()
        y2 = landmark.bottom()
        #cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

        landmarks = predictor(gray, landmark)

        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(img, (x, y), 2, (50, 255, 20), -1)


    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
