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

def sayText(text):
    talking = True
    tts = gTTS(text=text, lang='en')
    print(text)
    tts.save("tempText.mp3")
    os.system("mpg123 tempText.mp3")
    talking = False

# Main Thread

while True:
    if connected:
        data = arduino.read()
        ioValue = data
        print(ioValue[0])
        if "1" in ioValue:
            if tasks:
                task = tasks[0]
                print("Talking")
                sayText("Start %s for %d mins." % (task["name"], task["time"]))
            else:
                sayText("Please add a task to the app.")
            ioValue = "."
        if "0" in ioValue:
            print("Goodbye")
            sayText("Goodbye!")
            ioValue = "."
    else:
        print("E: not connected to wifi")

    sleep(0.05)
