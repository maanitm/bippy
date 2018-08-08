from tkinter import *
import datetime
from gtts import gTTS
import time
import os
import threading
import curses

name = "Owen"
task = "math problems"
totalTime = 120

# textsToSpeak = ["Hi, %s. My name is Bippy. We’re going to do a short and easy task today, it’s very important for me! We are going to do %s. The color of the screen will change to show how much time you have left. But do not worry, you will do great. Let's start now. " % (name, task), "Wow you are working well! Remember, completing %s is very important for me!" % task, "Keep up the good work, %s!" % name, "Your doing great. Keep working on %s. I am really proud of you." % task, "You are SO close to completing your %s." % task, "I hope you are learning a lot.", "You are almost done! Great job, %s" % name, "Great job today, %s! We are going to take a break now. See you later!" % name]

textsToSpeak = [
    "Hello, %s, my name is Bippy. Today, we are just going to do a few short tasks. Then, you can take a break for your hard work! Are you ready?" % name,
    "Okay great! There are a few math questions in front of you. We are going to start the first five questions now. Show it to me whenever you are ready.",
    "You are doing great!",
    "Good job! Keep up the good work!",
    "Okay, are you ready to show me?",
    "Alright, can I see your answer?",
    "Wonderful! Let’s move on to the next five questions. Show me whenever you are ready",
    "Amazing! Let’s take a short break now! I’ll tell you when to start again.",
    "Are you sure that is the correct answer?",
    "Great job! We are all done. Thank you, %s!" % name
]

currentTime = 0

def sayText(text):
    tts = gTTS(text=text, lang='en')
    tts.save("text.mp3")
    os.system("afplay text.mp3")

def repeatSay():
    win = curses.initscr()
    # Turn off line buffering
    curses.cbreak()

    # Initialize the terminal
    
# 048,149,250,351,452,553,654,755,856,957
    # Make getch() non-blocking
    win.nodelay(True)
    while True:
        # if currentTime == totalTime:
        #     sayText("Goodbye!")
        # elif currentTime % (totalTime/len(textsToSpeak)) == 0:
        #     sayText(textsToSpeak[int(currentTime/(totalTime/len(textsToSpeak)))])
        key = win.getch()
        if key != -1:
            num = int(str(key)) - 48
            sayText(textsToSpeak[int(num)])
        time.sleep(0.01)

frame = Frame(width=1440, height=800, bg="red", colormap="new")
frame.pack()

start = datetime.datetime.now()

gaps = totalTime / len(textsToSpeak)
gaps = round(gaps, 0)
prevTime = 0

# while True:
#     current = datetime.datetime.now()
#     duration = current - start
#     durationSecs = duration.total_seconds()
#     durationSecs = round(durationSecs, 0)
#     if durationSecs != prevTime:
#         if durationSecs % gaps == 0:
#             sayText(textsToSpeak[int(durationSecs / gaps)-1])
#     prevTime = durationSecs

t = threading.Thread(target=repeatSay)
t.daemon = True
t.start()

currentRgb = (0, 0, 0)
for i in range(totalTime+1):
    time.sleep(1)
    currentTime = i
    currentRgb = (int(i*(255/totalTime)), 255, 0)

    if i > totalTime/2:
        # print(255-int(i*(255/totalTime))))
        currentRgb = (255, 255-int((i-(totalTime/2))*(255/totalTime)), 0)

    frame.config(bg="#%02x%02x%02x" % currentRgb)
    
    print(currentTime)
    frame.update()