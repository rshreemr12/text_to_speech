# It works offline, unlike other text-to-speech libraries. 
# Rather than saving the text as audio file, pyttsx actually speaks it there. 
# This makes it more reliable to use for voice-based projects.

# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()

# testing
engine.say("My first code on text-to-speech")
engine.say("Built by Ramya, welcome !")
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

sen = """Too bored to read the books yourself ?
        Are you driving ? or travelling ? cant get youself a seat ?
        Let this bot read it for you. 
        All that needs to be done is scrape the data and bring it here.
        Rest is taken care. """


engine.say(sen)
engine.runAndWait()
