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

# Functions
def readIo():
    global ioValue
    while True:
        data = arduino.read()
        print(data)
        ioValue = data

def sayText(text):
    talking = True
    tts = gTTS(text=text, lang='en')
    print(text)
    tts.save("tempText.mp3")
    os.system("mpg123 tempText.mp3")
    talking = False

# Setup
arduinoThread = Thread(target=readIo)
arduinoThread.start()

# Main Thread

while True:
    if connected:
        print(ioValue)
        if ioValue in "1":
            if tasks:
                task = tasks[0]
                sayText("Start %s for %d mins." % (task["name"], task["time"]))
            else:
                sayText("Please add a task to the app.")
        if ioValue in "0":
            sayText("Goodbye!")
    else:
        print("E: not connected to wifi")
