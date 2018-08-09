from gtts import gTTS
import os

name = "Owen"
task = "math problems"
totalTime = 120

textsToSpeak = [
    "Hello, %s, my name is Bippy. Today, we are just going to do a few short tasks. Then, you can take a break for your hard work! Are you ready?" % name,
    "Okay great! There are a few math questions in front of you. We are going to start the first five questions now. Show it to me whenever you are ready.",
    "You are doing great!",
    "Good job! Keep up the good work!",
    "Okay, are you ready to show me?",
    "Alright, can I see your answer?",
    "Wonderful! Let's move on to the next five questions. Show me whenever you are ready",
    "Amazing! Let's take a short break now! I'll tell you when to start again.",
    "Are you sure that is the correct answer?",
    "Great job! We are all done. Thank you, %s!" % name
]


def sayText(text):
    tts = gTTS(text=text, lang='en')
    tts.save("text.mp3")
    os.system("mpg321 text.mp3")

sayText("hello there maanit")