from threading import Thread
import serial
# from picamera import PiCamera
from time import sleep
from gtts import gTTS
import os

# camera = PiCamera()

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)

running = False
clickCamera = False
speak = False
textToSpeak = ""

def sayText(text):
    tts = gTTS(text=text, lang='en')
    tts.save("text.mp3")
    os.system("mpg321 text.mp3")

def writeLoop():
    global running
    while True:
        arduino.write(bytes("test", encoding='utf-8'))
        sleep(5)

def speakLoop():
    global running, speak
    while True:
        # speak words here
        if speak:
            sayText(textToSpeak)
            speak = False

def cameraLoop():
    global running, clickCamera
    while True:
        if clickCamera:
            # camera.start_preview()
            sleep(3)
            # camera.capture('/home/pi/bippy/tmp_img.jpg')
            # camera.stop_preview()
            println("clicked picture")
            sayText("Great job Maanit!")
            clickCamera = False

def tasksLoop():
    global running
    while True:
        # get tasks here
        println()

writeThread = Thread(target=writeLoop)
speakThread = Thread(target=speakLoop)
cameraThread = Thread(target=cameraLoop)
tasksThread = Thread(target=tasksLoop)

writeThread.start()
speakThread.start()
cameraThread.start()
tasksThread.start()

while True:
    data = arduino.read()
    print(data)
    if data in "0":
        print("stop")
        running = False
    if data in "1":
        print("start")
        running = True
    if data in "2":
        print("motivate")
        textToSpeak = "You are doing great! Keep up the good work!"
        speak = True
    if data in "3":
        print("camera")
        clickCamera = True
    if data in "4":
        print("done")
        textToSpeak = "Great job today! See you later."
        speak = True
