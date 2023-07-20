import cowsay
import pyttsx3
import sys

engine = pyttsx3.init()
this = input("What is this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()





if len(sys.argv) == 2: 
    cowsay.trex("hello, " + sys.argv[1])
    cowsay.cow("hello, " + sys.argv[1])