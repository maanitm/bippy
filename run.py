import thread
import serial
# from picamera import PiCamera
from time import sleep
from gtts import gTTS

# camera = PiCamera()

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)

writeThread = thread.Thread(target=writeLoop)
speakThread = thread.Thread(target=speakLoop)
cameraThread = thread.Thread(target=cameraLoop)
tasksThread = thread.Thread(target=tasksLoop)

running = False 
clickCamera = False
speak = False
textToSpeak = ""

def sayText(text):
    tts = gTTS(text=text, lang='en')
    tts.save("demoText.mp3")
    os.system("mpg321 demoText.mp3")

def writeLoop():
    while running:
        arduino.write(bytes("test", encoding='utf-8'))
        sleep(5)
    
def speakLoop():
    while running:
        # speak words here
        if speak:
            sayText(textToSpeak)
            speak = False
        
def cameraLoop():
    while running:
        if clickCamera:
            # camera.start_preview()
            sleep(3)
            # camera.capture('/home/pi/bippy/tmp_img.jpg')
            # camera.stop_preview()
            println("clicked picture")
            sayText("Great job Maanit!")
            clickCamera = False

def tasksLoop():
    while running:
        # get tasks here
        println()

while True:
    data = arduino.read()
    if data == 0:
        print("stop")
        running = False
    if data == 1:
        print("start")
        running = True
    if data == 2:
        print("motivate")
        textToSpeak = "You are doing great! Keep up the good work!"
        speak = True
    if data == 3:
        print("camera")
        clickCamera = True
    if data == 4:
        print("done")
        textToSpeak = "Great job today! See you later."
        speak = True