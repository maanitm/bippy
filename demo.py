import thread
import serial
# from picamera import PiCamera
from time import sleep
from gtts import gTTS
import os
# camera = PiCamera()

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)

#tts = gTTS(text="Hi. I am Bippy. Are you ready to start summer reading?", lang='en')
#tts.save("demoText.mp3")
#os.system("mpg321 demoText.mp3")

while True:
    data = arduino.read()
    if data == 0:
        print("stop")
    if data == 1:
        print("start")
        os.system("mpg321 demoText.mp3")
    
