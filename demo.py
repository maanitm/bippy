import serial
from gtts import gTTS
import os

# arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)

tts = gTTS(text="Hi. I am Bippy. Do you have any questions?", lang='en')
tts.save("demoText.mp3")
os.system("afplay demoText.mp3")