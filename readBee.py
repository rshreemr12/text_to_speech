# It works offline, unlike other text-to-speech libraries. 
# Rather than saving the text as audio file, pyttsx actually speaks it there. 
# This makes it more reliable to use for voice-based projects.

# importing the pyttsx library
import pyttsx3
import os 

path_to_read = ".\Data\sample_read.txt"

# initialisation
engine = pyttsx3.init()

# testing
engine.say("Welcome !")
engine.say("Built by Ramya")
engine.runAndWait()



def onStart():
    print('starting')

def onWord(name, location, length):
    print('word', name, location, length)

def onEnd(name, completed):
    print('finishing', name, completed)

engine = pyttsx3.init()

engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)


try:
    with open(path_to_read ,'r') as fd:
        sen = fd.readlines()
except Exception as err:
    print("Error: ", err )
    sen = "Error occured lets try again"


engine.say(sen)
engine.runAndWait()
