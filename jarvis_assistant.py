
import pyttsx3
import speech_recognition as sr

import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
#print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hello mr. vikash I am jarvis your personal assistant")

def take_command():#
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        #r.pause_threshold = 1
        #audio = r.listen(source)
    #try:
        #print("Recognizing... ")
        #query = r.recognize_google(audio, Language="en-in")
        #print(f"user said: {query}\n")
    #except Exception as e:
        #print(e)
        #print("say that again please...")
        #return "NONE"
    #return query

if __name__ == "__main__":
    #speak("vikash is a good boy")
    #Wish_me()
    take_command()
