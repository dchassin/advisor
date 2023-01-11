# Python program to translate
# speech to text and text to speech
#
# Mac install
# $ brew install portaudio
# $ pip install -r requirements.txt
 
import os, json
import speech_recognition as sr
import pyttsx3
import advise

advise.FORCE = True

try:
    with open(f"config.json","r") as fh:
        config = json.load(fh)
except Exception as err:
    print("ERROR:",err)
    config = {
        "name" : os.getenv('USER').title(),
        "voice" : "Alex"
    }
NAME = config["name"]
VOICE = config["voice"]
 
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
engine = pyttsx3.init()
engine.setProperty('voice',f"com.apple.speech.synthesis.voice.{VOICE}")
def SpeakText(command):
     
    # Initialize the engine
    engine.say(command)
    engine.runAndWait()
     
with sr.Microphone() as source:

    print("Calibrating...",flush=True)     
    r.adjust_for_ambient_noise(source, duration=1)
     
    SpeakText(f"Hello {NAME}")

    while(1):   
         
        try:
             
            # use the microphone as source for input.
            
            print("Listening...",flush=True)
            audio = r.listen(source)
             
            print("Recognizing...",flush=True)
            query = r.recognize_google(audio)

            if query.lower() == "goodbye":
                break

            print("Thinking...",flush=True)
            reply = advise.query(query)
 
            print(f"Replying...",flush=True)
            SpeakText(reply)
             
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
             
        except sr.UnknownValueError:
            print("unknown error occurred")

SpeakText(f"Goodbye {NAME}")