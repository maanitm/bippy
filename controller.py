from threading import Thread
import serial
# from picamera import PiCamera
from time import sleep
from gtts import gTTS
import os

# Notes
# IO Values - 0:Stop, 1:Start, 2:

# Constants
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)

# Variables
connected = True
ioValue = "."
tasks = [{"name":"Math work", "time":30}]
name = "Maanit"

# Functions

def sayText(text):
    talking = True
    tts = gTTS(text=text, lang='en')
    print(text)
    tts.save("tempText.mp3")
    os.system("mpg123 tempText.mp3")
    talking = False

# Main Thread
startedActivity = False
speechVar1 = ""
currentTask = -1
textsToSpeak = [
    "Hello, %s, my name is Bippy. Today, we are just going to do a few short tasks. Then, you can take a break for your hard work!" % name,
    "We are going to start %s now. Show it to me whenever you are ready.",
    "You are doing great!",
    "Good job! Keep up the good work!",
    "Okay, are you ready to show me?",
    "Alright, can I see your answer?",
    "Wonderful! Let's move on to the next five questions. Show me whenever you are ready",
    "Amazing! Let's take a short break now! I'll tell you when to start again.",
    "Are you sure that is the correct answer?",
    "Great job! We are all done. Thank you, %s!"
]
while True:
    if connected:
        data = arduino.read()
        ioValue = data
        print(ioValue[0])
        if "1" in ioValue:
            if tasks:
                currentTask = 0
                startedActivity = True
            else:
                sayText("Please add a task to the app.")
            ioValue = "."
        if "0" in ioValue:
            sayText("Goodbye!")
            ioValue = "."
            startedActivity = False
        
        if startedActivity:
            speechVar1 = name
            sayText(textsToSpeak[0])
            speechVar1 = tasks[currentTask]["name"]
            sayText(textsToSpeak[1] % tasks[currentTask]["name"])
            startedActivity = False

    else:
        print("E: not connected to wifi")

    sleep(0.05)
