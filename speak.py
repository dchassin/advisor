# Python program to translate
# speech to text and text to speech
#
# Mac install
# $ brew install portaudio
# $ pip install pyaudio
# $ pip install pyttsx3
# $ pip install speechrecognition
 
import os
import speech_recognition as sr
import pyttsx3
 
# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
     
# Loop infinitely for user to
# speak
 
while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=1)
             
            SpeakText(f"Hello {os.getenv('USER').title()}")

            #listens for the user's input
            audio = r.listen(source)
            print("...",flush=True)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
 
            print(f"Did you say {MyText}?",flush=True)
            SpeakText(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")