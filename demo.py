import thread
import serial
# from picamera import PiCamera
from time import sleep
from gtts import gTTS

# camera = PiCamera()

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)

while True:
    data = arduino.read()
    if data == 0:
        print("stop")
    if data == 1:
        print("start")
        os.system("mpg321 demoText.mp3")
    