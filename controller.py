from threading import Thread
import serial
from picamera import PiCamera
from time import sleep
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
    arduino.write('r255;g255;b255;')
    println("on")
    sleep(0.5)
    arduino.write('r000;g000;b000;')
    println("off")
    sleep(0.5)
    arduino.write('r255;g255;b255;')
    println("on")
    sleep(0.5)
    arduino.write('r000;g000;b000;')
    println("off")
    sleep(0.5)
    arduino.write('r255;g255;b255;')
    println("on")
    camera.capture('tempImage.jpg')
    println("capture")
    sleep(0.5)
    arduino.write('r000;g000;b000;')
    println("off")

# Main Thread
startedActivity = False
currentTask = -1
intro = True
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
    if connected:
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
            arduino.write('r122;')
            
            intro = False

    else:
        print("E: not connected to wifi")

    sleep(0.05)
