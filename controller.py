from threading import Thread
import serial
# from picamera import PiCamera
from time import sleep
from gtts import gTTS
import os

# Notes
# IO Values - 1:Start, 2:

# Constants
# arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
arduinoThread = Thread(target=readIo)

# Variables
connected = True
ioValue = 1
tasks = [{"name":"Math HW", "time":30}]

# Functions
def readIo():
    global ioValue
    data = "1"#arduino.read()
    print(data)
    ioValue = int(data)

def sayText(text):
    talking = True
    tts = gTTS(text=text, lang='en')
    tts.save("tempText.mp3")
    os.system("mpg123 tempText.mp3")
    talking = False

# Setup
arduinoThread.start()

# Main Thread

while True:
    if connected:
        if ioValue == 1:
            if tasks:
                for task in tasks:
                    sayText("Start %s for %d mins." % (task["name"], task["time"]))
                    
            else:
                sayText("Please add a task to the app.")
    else:
        print("E: not connected to wifi")
