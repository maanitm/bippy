from threading import Thread
import serial
from picamera import PiCamera
from time import sleep
import time
from gtts import gTTS
import os

from parse_rest.datatypes import Object
from parse_rest.connection import register
from parse_rest.user import User

# Notes
# IO Values - 0:Stop, 1:Start, 2:Click

# Constants
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
camera = PiCamera()
os.environ["PARSE_API_ROOT"] = "http://54.145.224.112:1337/parse"

APPLICATION_ID = 'ebbb3fa530a6a5df5dcf5c6a1c13820c717b48f7'
REST_API_KEY = 'bippy123'
MASTER_KEY = 'b374d90f0bee2c48f33462b395ae2d6d0adebebd'

register(APPLICATION_ID, REST_API_KEY, master_key=MASTER_KEY)

u = User.signup("maanitm", "12345", phone="678-641-7374")

# Variables
connected = True
data = "."
tasks = [{"name":"Math work", "time":2}, {"name":"English questions", "time":60}]
name = "Maanit"

# Functions

def sayText(text):
    talking = True
    tts = gTTS(text=text, lang='en')
    print(text)
    tts.save("tempText.mp3")
    os.system("mpg123 tempText.mp3")
    talking = False

def takePicture():
    sleep(2)
    camera.capture('tempImage.jpg')
    sleep(1)

# Main Thread
startedActivity = False
currentTask = -1
data = "."
intro = True
startTime = 0
currentTime = 0
textsToSpeak = [
    "Hello, %s, my name is Bippy. Today, we are just going to do a few short tasks. Then, you can take a break for your hard work!" % name,
    "We are going to start %s now. Show it to me whenever you are ready.",
    "You are doing great!",
    "Good job! Keep up the good work!",
    "Okay, are you ready to show me?",
    "Alright, can I see your work?",
    "Wonderful! Let's move on to the next task. We are going to do %s now. Show me whenever you are ready",
    "Amazing! Let's take a short break now! I'll tell you when to start again.",
    "Are you sure that is the correct answer?",
    "Great job! We are all done. Thank you, %s!" % name,
    "Goodbye!",
    "Please add a task to the app."
]

def readArduino():
    global data
    data = arduino.read()
    sleep(0.05)

readThread = Thread(target=readArduino)
readThread.start()

while True:
    if connected:
        currentTime = time.time()
        print(data[0])
        if data in "1":
            if tasks:
                currentTask = 0
                startedActivity = True
            else:
                sayText(textsToSpeak[11])
            data = "."
        if data in "0":
            sayText(textsToSpeak[10])
            data = "."
            startedActivity = False
        if  data in "2" and startedActivity:
            sayText(textsToSpeak[5])
            takePicture()
            if len(tasks) > currentTask + 1:
                currentTask += 1
                sayText(textsToSpeak[6] % tasks[currentTask]["name"])
            else:
                sayText(textsToSpeak[9])
                startedActivity = False
            data = "."
        
        if startedActivity and intro:
            sayText(textsToSpeak[0])
            sayText(textsToSpeak[1] % tasks[currentTask]["name"])
            startTime = time.time()
            intro = False
        # print(startedActivity)
        if startedActivity and not intro:
            elapsed = currentTime - startTime
            total = float(tasks[currentTask]["time"]) * 60.0
            print(total - elapsed)
            currentRgb = (0, 0, 0)
            if elapsed > total/2 and elapsed < 9*total/10:
                # print(255-int(i*(255/totalTime))))
                currentRgb = (0, 255, 255)
            elif elapsed < total/2:
                currentRgb = (0, 255, 0)
            else:
                currentRgb = (255, 0, 0)
            # print(currentRgb)
            print('r{0:0=3d};g{1:0=3d};b{2:0=3d};'.format(currentRgb[0], currentRgb[1], currentRgb[2]))
            # arduino.write('r{0:0=3d};g{1:0=3d};b{2:0=3d};'.format(currentRgb[0], currentRgb[1], currentRgb[2]))
            if elapsed >= total:
                data = "2"
    else:
        print("E: not connected to wifi")
