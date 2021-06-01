# Desktop-Assistant features

- Try implementing it by switch case
- we can also add face recognisition so the comp says hello as soon as it sees our face.
- Add news api in this & weather api, #83 video
- Place a call on teams/duo or something
- Should stop talking if i say "STOP"
- It should read a word doc or pdfs if we ask her to

- Add a "what can I do for you" section
- Add games
- Add that when we say "Hello Hazel/Wake up Hazel", the program will automatically start

- Play the user recommended song
- Add workout music
- Add a feature to replay the same song if i want, or change song, pause, play
- Add shazm or some song recognition software


- if its morning and its the first time i open the program, so it can say "Hope you had a goodnights sleep."
- Switch off the pc / restart the pc on command
- Add "Wake up" and "sleep" functions.
- Can add a feature that if for some reason its not able to recognize what we say, 
  we can type it in the console and then it will perform that task

- Can differentiate between me and other people, and if possible store their voices.
- Gets activated by me or my family members, no one else.
- Digital calender , open calender
- Understand hindi, or a few other languages, i can have the command "switch to hindi" 
  or it can directly understand that im speaking in hindi and will switch by itself
- Add a translator
- open new word doc, or ppt
- change your wallpaper/other background
- unlock pc by verbally saying the password

- Analyse my commands and give suggestions in the future

Code for news api:
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)

if _name_ == '__main__':
    import requests
    import json
    url = ('https://newsapi.org/v2/top-headlines?'

           'sources=bbc-sport&'
           'apiKey=49e391e7066c4158937096fb5e55fb5d')

    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0, 11):
        speak(my_json['articles'][i]['title'])
