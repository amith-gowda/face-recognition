# Import OpenCV2 for image processing
import cv2
import os
import time
import RPi.GPIO as GPIO
import cv2

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

##cap = cv2.VideoCapture(0)

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

IN1=21
IN2=20
IN3=12
IN4=16
LOCK = 2
SW = 3
LED = 4                                  

GPIO.setup(LOCK,GPIO.OUT)
GPIO.setup(SW,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

GPIO.output(LOCK, False)

GPIO.output(LED, False)

def FORWARD():
    print('FORWARD')
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    time.sleep(2)


def STOP():
    print('STOP')
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

# Import numpy for matrices calculations
import numpy as np
import time
import datetime
import sys
import time
import random
import datetime
import telepot

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath)

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

flag = []
count1=0
count2=0
count3=0
sample =0
lecture=0
mon=0
count=0
def switch():
    GPIO.output(LED,True)
    if(GPIO.input(SW)==False):
           print('22222')


    
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
   
    print ('Got command: %s' % command)

    if command == '*1234':
       bot.sendMessage(chat_id, str('Permission Granted'))
       print('Permission Granted')
       GPIO.output(LOCK,True)
       FORWARD()
       time.sleep(2)
 
    else:
       bot.sendMessage(chat_id, str('Permission Denied'))
       print('Permission Denied')
       GPIO.output(LOCK,False)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):    
    im = frame.array
    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    rawCapture.truncate(0)
    
    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id,i = recognizer.predict(gray[y:y+h,x:x+w])
        #id = int(os.path.split(imagePath)[-1].split(".")[1])
        
        print(i)
        # Check the ID if exist
        if i < 50:
            sample= sample+1
            if Id == 1:
                #flag[1]=1
                count1=1
                Id = "1"
                print("1")
                lecture=1
                sample=0
                GPIO.output(LOCK, GPIO.HIGH)
                FORWARD()
                time.sleep(2)
                cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
                cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)
                cv2.imshow('im',im)
                break
            
        else:
            count=count+1
            Id = "unknown"

            if count > 10:
                count=0
                print(Id)
                mon=0
                Id = "unknown"
                STOP()
                print('UNKNOWN PERSON DETECTED')
                GPIO.output(LOCK, GPIO.LOW)
                time.sleep(5)
                cv2.imwrite('frame.png',im)
                bot = telepot.Bot('')   #enter telegram api key here
                bot.sendMessage("792235296", str('Unknown person detected. Waiting for response.'))
                bot.message_loop(handle)
                print ('Listening...')
        
        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)
        cv2.imshow('im',im)

        # Display the video frame with the bounded rectangle
    cv2.imshow('im',im)


    # If 'q' is pressed, close program
    if cv2.waitKey(20) & 0xFF == ord('q'): #if cv2.waitKey(10) & 0xFF == ord('q'):
        break
           
cam.release()

# Close all windows
cv2.destroyAllWindows()
