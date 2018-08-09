from gtts import gTTS
import os

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


def sayText(text):
    tts = gTTS(text=text, lang='en')
    tts.save("text.wav")
    os.system("afplay text.wav")

sayText("hello there maanit")