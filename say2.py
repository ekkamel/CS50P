import pyttsx3

engine = pyttsx3.init()
this = input("What is this? ")
engine.say(this)
engine.runAndWait()
