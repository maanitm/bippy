import serial
from gtts import gTTS
import os

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)

tts = gTTS(text="Hi. I am Bippy. Are you ready to start summer reading?", lang='en')
tts.save("demoText.mp3")
#os.system("mpg321 demoText.mp3")

while True:
    data = arduino.read()
    print(data)
    if b'0' in data:
        print("stop")
    if b'1' in data:
        print("start")
        os.system("mpg321 demoText.mp3")
    
