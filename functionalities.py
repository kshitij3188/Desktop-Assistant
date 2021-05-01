# Google Calendar API imports
from __future__ import print_function
import datetime
from datetime import date
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Module imports
import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib                              #simple mail transfer   
import subprocess
import random
import pyjokes
import datetime
import time
import pyautogui



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


engine = pyttsx3.init('sapi5')   # used for getting voice which is inbuilt in window
voices = engine.getProperty('voices')   # getting details of current voices
# print(voices)    so there are various voices(male/female)
engine.setProperty('voice',voices[1].id)
# print(voices[1].id)           hazel



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# greet acc to time
# Todo : after 12am, it wishes me gm instead of gn
# Check code at 12 pm
# Add the time also: i.e. what time is it?

def usrname():
    speak("What should i call you?")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)

def wishMe():
    hour = int(datetime.datetime.now().hour)
   
    if (hour >= 0 and hour < 5) or (hour > 22):
        speak("Good night, have a nice sleep")
    elif hour >= 5 and hour < 12:
        speak("Good morning, how are you today?")
    elif hour >=12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening, hope you had a nice day")
    speak("I am Hazel, How may I help you?")
    

# It takes microphone input from user & returns string output
def takeCommand():
    r = sr.Recognizer()                                 # this class will help recognize the audio
    with sr.Microphone() as source:                     # its using our microphone as source
        print("Listening...")
        
        # Todo: Here i can also increase the energy_threshold so that it will only listen when i speak loudly
        r.pause_threshold = 1                           # seconds of non-speaking audio before the phrase is considered complete
        audio = r.listen(source)                        # Todo (Have a look)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # speak("You said:")
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        
        return "None"           # returning a none string

    return query.lower()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()                                               #Transport layer security
    server.login("poojarmangal@gmail.com", "pooh456321")
    server.sendmail('poojarmangal@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    
    # Greet us
    #wishMe()
    myName = "Hazel"
    # usrname()
    
    #speak("Hello I'm Pooja's new assistant, Hazel")
     

    while True:
        query = takeCommand()
        # Logic for executing tasks based on query

        # Conversations
        if 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you?")
        elif 'fine' in query or 'okay' in query or 'good' in query or 'great' in query:
            speak("Its nice to hear that") 
        elif 'unhappy' in query or "i'm sad" in query:
            speak("Its sad to know that, do you want me to play some music for you?")
            yes_no = takeCommand()
            if 'yes' in yes_no:
                speak("Playing music")
                music_dir = 'D:\\songs\\sad'
                songs = os.listdir(music_dir)           #lists all the files in music directory
                print(songs)
                random = random.randint(0, len(songs))
                os.startfile(os.path.join(music_dir,songs[random]))
            elif 'no' in yes_no:
                speak("Okay, I'm here if you need me")
        elif 'thank you' in query:
            speak("You're most welcome")

        elif "what's your name" in query or "What is your name" in query :
            speak("My friends call me")
            speak(myName)
            print("My friends call me", myName)
        elif 'who are you' in query:
            speak("I am a desktop assitant created by Pooja")
        
        
        # elif "change name" or 'i dont like your name':
        #     speak("What would you like to call me?")
        #     myName = takeCommand()
        #     speak("Thank you for naming me, from now on I am")
        #     speak(myName)
        
        elif "what do you do" in query or 'what is your job' in query or 'whats your job' in query:
            speak("I am")
            speak(myName)
            speak("Your desktop assistant")
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Pooja.")
        
        elif "i am bored" in query:
            speak("I could play some music or open youtube. What can i do for you?")
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        # Performing tasks
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia, ")
            print(results)
            speak(results)

        # Opening websites
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        # Playing music
        
        elif 'play music' in query or 'play songs' in query:
            speak("What type of music would you like me to play?")
            music_type = takeCommand()  
            if 'sad music' in music_type:
                speak("Playing music")
                music_dir = 'D:\\songs\\sad'
                songs = os.listdir(music_dir)           #lists all the files in music directory
                print(songs)
                random = random.randint(0, len(songs))
                os.startfile(os.path.join(music_dir,songs[random]))         
            elif 'romantic music' in music_type:
                speak("Playing music")
                music_dir = 'D:\\songs\\romantic'
                songs = os.listdir(music_dir)           #lists all the files in music directory
                print(songs)
                random = random.randint(0, len(songs))
                os.startfile(os.path.join(music_dir,songs[random]))      
            elif 'dance' in music_type or 'party music' in music_type:
                speak("Playing music")
                music_dir = 'D:\\songs\\party'
                songs = os.listdir(music_dir)           #lists all the files in music directory
                print(songs)
                random = random.randint(0, len(songs))
                os.startfile(os.path.join(music_dir,songs[random]))  
        elif 'increase volume' in query:
            for i in range(5):
                pyautogui.press('volumeup')
        elif 'decrease volume' in query:
            for i in range(5):
                pyautogui.press('volumedown')

        # Make it say the proper time after 12pm
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        
        #todays date/ tomorrows date
        elif 'date' in query:
            speak(f"Today's date is {date.today()}")

        
            




        # Work on this
        elif 'open teams' in query:
            teamsPath = "C:\\Users\\pooja\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams"
            os.startfile(teamsPath)
        elif 'open discord' in query:
            discordPath = "C:\\Users\\pooja\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord"
            os.startfile(discordPath)
        elif 'open notepad' in query:
            speak("Opening your notepad")
            notePath = "D:\\studies\\Project\\Python\\all_projects.txt"
            os.startfile(notePath)

        # Todo : Make a dict of ppl you want to send emails to & do that
        # MAKE THIS OKAY, THAT IF A USER SAYS A MESAGE AND ITS INCORRECT, AND AGAIN WHEN HE SAYS IT , ITS INCORRECT, SO THERE SHOULD BE AN OPTION.
        elif 'email to pooja' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                print(content)
                speak("is this correct? Kindly confirm")
                confirm = takeCommand()
                if 'yes' in confirm:
                    to = 'poojarmangal@gmail.com'
                    sendEmail(to, content)
                    speak("Email sent!")
                elif 'no' in confirm:
                    speak("I am sorry, kindly say your message again")
                    
                # Todo: Have a email correction option

            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")

        elif 'send an email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should i send it to?")
                to = input()    
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        # elif 'search' in query or 'play' in query:
             
        #     query = query.replace("search", "") 
        #     query = query.replace("play", "")          
        #     webbrowser.open(query) 









        # Take time in seconds, mins and hrs
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            speak("I am back")
        elif 'lock window' in query: 
            cmd='rundll32.exe user32.dll, LockWorkStation'
            subprocess.call(cmd)
        elif 'shutdown' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        
        elif 'empty recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Emptied")
            except:
                speak("Your recycle bin is already empty")   
    
        elif 'exit' in query or 'quit' in query:
            speak("Exiting, thank you for giving me your time")
            exit()

        