from unittest import result
import webbrowser
import pyttsx3 
import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id )



def speak(audio): 
    engine.say(audio)
    engine.runAndWait()
from datetime import datetime     
def wishMe():
    hour = datetime.now().hour
    if hour>=0 and hour<12:
        speak ("Good morning Mahima ")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon Mahima !")
    else: 
        speak("Good Evening") 
    speak ("I am Jarvis sir. Please tell me !  how may i help you ")
import speech_recognition as sr 
from random import choice 

def takeCommand():

    #It take microphone input from the user and returns string output 
    r = sr.Recognizer()
    with sr.Microphone( ) as source :
        print("Listening...") 
        r.pause_threshold =  1
        audio = r.listen(source)
    try :
        print("Recognizing...")
        query = r.recongnize_google(audio, language='en-in')
        print (f"User said: {query}\n")
    except Exception as e :
        print("Say that again please...")
        return "None "     
    return query 
if __name__=="__main__" :
    wishMe()
    while True : 
        query = takeCommand().lower()
        #Logic for excuting tasks based in query 
        if'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 1 )
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")    
        elif 'open Google ' in query:
            webbrowser.open("Google.com") 
        elif 'open stackoverflow ' in query:
            webbrowser.open("stackoverflow.com")
            




    
             
        

        
 


    






