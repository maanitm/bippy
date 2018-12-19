from threading import Thread
import serial
from picamera import PiCamera
from time import sleep
import time
from gtts import gTTS
import os

# Notes
# IO Values - 0:Stop, 1:Start, 2:

# Constants
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
camera = PiCamera()

# Variables
connected = True
ioValue = "."
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
    arduino.write('r255;')
    arduino.write('g255;')
    arduino.write('b255;')
    print("on")
    sleep(1)
    arduino.write('r000;')
    arduino.write('g000;')
    arduino.write('b000;')
    print("off")
    sleep(1)
    arduino.write('r255;')
    arduino.write('g255;')
    arduino.write('b255;')
    print("on")
    sleep(1)
    arduino.write('r000;')
    arduino.write('g000;')
    arduino.write('b000;')
    print("off")
    sleep(1)
    arduino.write('r255;')
    arduino.write('g255;')
    arduino.write('b255;')
    print("on")
    camera.capture('tempImage.jpg')
    print("capture")
    sleep(1)
    arduino.write('r000;')
    arduino.write('g000;')
    arduino.write('b000;')
    print("off")

# Main Thread
startedActivity = False
currentTask = -1
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
while True:
    print("a")
    if connected:
        currentTime = time.time()
        data = arduino.read()
        ioValue = data
        print(ioValue[0])
        if ioValue in "1":
            if tasks:
                currentTask = 0
                startedActivity = True
            else:
                sayText(textsToSpeak[11])
            ioValue = "."
        if ioValue in "0":
            sayText(textsToSpeak[10])
            ioValue = "."
            startedActivity = False
        if  ioValue in "2" and startedActivity:
            sayText(textsToSpeak[5])
            takePicture()
            if len(tasks) > currentTask + 1:
                currentTask += 1
                sayText(textsToSpeak[6] % tasks[currentTask]["name"])
            else:
                sayText(textsToSpeak[9])
                startedActivity = False
            ioValue = "."
        
        if startedActivity and intro:
            sayText(textsToSpeak[0])
            sayText(textsToSpeak[1] % tasks[currentTask]["name"])
            startTime = time.time()
            intro = False
        print(startedActivity)
        print(currentTime)
        if startedActivity and not intro:
            elapsed = currentTime - startTime
            total = float(tasks[currentTask]["time"]) * 60.0
            currentRgb = (int(elapsed*(255/total)), 255, 0)
            if elapsed > total/2:
                # print(255-int(i*(255/totalTime))))
                currentRgb = (255, 255-int((elapsed-(total/2))*(255/total)), 0)
            print(currentRgb)
            print('r{0:0=3d};g{0:0=3d};b{0:0=3d};'.format(currentRgb[0], currentRgb[1], currentRgb[2]))
            arduino.write('r{0:0=3d};g{0:0=3d};b{0:0=3d};'.format(currentRgb[0], currentRgb[1], currentRgb[2]))

    else:
        print("E: not connected to wifi")

    # sleep(0.05)
