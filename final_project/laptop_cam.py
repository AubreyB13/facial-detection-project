import cv2
import numpy as np
# from keras.models import load_model
# import pandas as pd
# import numpy as np
# import keras
# import pickle
# import IPython
# import matplotlib.pyplot as plt
# from keras.models import Sequential
# from keras.layers import Dense, Flatten, MaxPool2D, Conv2D
# from keras.models import Model

# from PIL import Image

#(720, 1280)

# cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier('faces.xml')

video_capture = cv2.VideoCapture(0)

#model = load_model('faceDetection.h5')

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()



    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    # cnn = model.predict(gray)
    # # Draw a rectangle around the faces
    # for (x, y, w, h) in cnn:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #     roi_gray = gray[y:y+h, x:x+w]
    #     roi_color = frame[y:y+h, x:x+w]
    # # Display the resulting frame
    # cv2.imshow('frame', frame)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
