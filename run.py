import thread
import serial
from picamera import PiCamera
from time import sleep
import gTTs

camera = PiCamera()

arduino = serial.Serial(port='/dev/cu.wchusbserial1420', baudrate=9600)

writeThread = thread.Thread(target=writeLoop)
speakThread = thread.Thread(target=speakLoop)
cameraThread = thread.Thread(target=cameraLoop)
tasksThread = thread.Thread(target=tasksLoop)

running = False 
clickCamera = False

def sayText(text):
    tts = gTTS(text=text, lang='en')
    tts.save("text.mp3")
    os.system("mpg321 text.mp3")

def writeLoop():
    while running:
        arduino.write(bytes("test", encoding='utf-8'))
        sleep(5)
    
def speakLoop():
    while running:
        # speak words here
        println()
        
def cameraLoop():
    while running:
        if clickCamera:
            camera.start_preview()
            sleep(3)
            camera.capture('/home/pi/bippy/tmp_img.jpg')
            camera.stop_preview()
            println("clicked picture")
            sayText("Great picture Maanit!")
            clickCamera = False

def tasksLoop():
    while running:
        # get tasks here
        println()

while True:
    data = arduino.read()
    if data == 0:
        print("start")
        running = True
    if data == 1:
        print("camera")
        clickCamera = True
    if data == 9:
        print("stop")
        running = False