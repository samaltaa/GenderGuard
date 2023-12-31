import cv2
import time
import datetime
import numpy as np
import pygame

#the gender model architecture
GENDER_MODEL = 'weights/deploy_gender.prototxt'

#the gender model pre-trained weights
GENDER_PROTO = 'weights/gender_net.caffemodel'

# Each Caffe Model impose the shape of the input image also image preprocessing is required like mean
# substraction to eliminate the effect of illunination changes
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

# Represent the gender classes
GENDER_LIST = ['Male', 'Female']
FACE_PROTO = "weights/deploy.prototxt.txt"
FACE_MODEL = "weights/res10_300x300_ssd_iter_140000_fp16.caffemodel"

#load face Caffe model
face_net = cv2.dnn.readNetFromCaffe(FACE_PROTO, FACE_MODEL)
#load gender prediction model
gender_net = cv2.dnn.readNetFromCaffe(GENDER_MODEL, GENDER_PROTO)

#function(s) for alarm triggering
def sound_alarm():
     pygame.mixer.init()
     pygame.mixer.music.load('alarm_sound.wav')
     pygame.mixer.music.play()

# define a video capture object
cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

detection = False 
detection_stopped_time = None
time_started = False
SECONDS_TO_RECORD_AFTER_FACE_DETECTED = 5

# define frame size 
frame_size = (int(cap.get(3)), int(cap.get(4)))
#define the codec
fourcc = cv2.VideoWriter_fourcc(*"mp4v")



while(True):

    #capture the video frame by frame 
    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor =1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    
    # this entire block of code takes care of beginning recoding once
    # face is detected, if face is undetected for 5+ seconds, recording stops
    if len(faces) > 0:
            if detection:
                 time_started = False
            else:
                 detection = True
                 current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                 video_filename = f"{current_time}.mp4"
                 out = cv2.VideoWriter(video_filename, fourcc, 20, frame_size)
                 print("Started Recording")
    elif detection:
         if time_started:
              if time.time() - detection_stopped_time > SECONDS_TO_RECORD_AFTER_FACE_DETECTED:
                   detection = False
                   time_started = False
                   out.release()
                   print("Recording Stopped")
         else:
            time_started = True
            detection_stopped_time = time.time()
    if detection:
        out.write(frame)

    # draw a rectangle around the faces detected 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        #crop the face region for gender detection
        face_roi = frame[y:y + h, x:x + w]

        #perform gender detection using the loaded model
        gender_blob = cv2.dnn.blobFromImage(face_roi, scalefactor=1.0, size=(227, 227), mean=MODEL_MEAN_VALUES, swapRB=True)
        gender_net.setInput(gender_blob)
        gender_preds = gender_net.forward()
        gender = GENDER_LIST[gender_preds[0].argmax()]

        #overlay the gender information on the frame
        cv2.putText(frame, f'Gender: {gender}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        #if a man is the frame, alarm goes off, otherwise it stops
        if gender == "Male":
            sound_alarm()
        else:
             break
                  

    #display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the quitting button 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
# after the loop release the cap object 
cap.release()
# destroy all the windows
cv2.destroyAllWindows()