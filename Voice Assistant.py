# Text to Speech conversion module
import pyttsx3
# Recognizing module
import speech_recognition as sr
#Libraries for doing tasks
import datetime
import os
from requests import get
import pywhatkit
import wikipedia
import json
import webbrowser



# SpeechApi
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[2].id)
engine.setProperty('voice', voice[1].id)


#Funtion to write new words in a json file("Brain")
def write(cmd, ans):
    with open('Brain.json') as jsonfile:
        decoded = json.load(jsonfile)
    decoded[str(cmd)] = str(ans)
    with open('Brain.json', 'w') as jsonfile:
        json.dump(decoded, jsonfile,indent=5)


# Speaking function

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Recognizing Function


def recognize():
    reco = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        reco.pause_threshold = 1
        audio = reco.listen(source, timeout=1, phrase_time_limit=3)

    try:
        print('Recognizing...')
        query = reco.recognize_google(audio, language='en-in')
        query = query.lower()
        if 'friday' in query:
            query = query.replace('friday', '')
        print('User said: ', query)
    except Exception as e:
        speak('Can you please repeat..')
        return 'none'
    return query

# Wishing


def wish():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 20:
        speak('Good Afternoon')
    else:
        speak('Good Night')

    speak('I am Friday, your personal Assistant')


if __name__ == '__main__':
    wish()
    while True:
        query=recognize()
        # To open apps:
        if 'notepad' in query:
            path = 'C:\WINDOWS\system32\\notepad.exe'
            os.startfile(path)

        if 'command' in query:
            # path = 'C:\WINDOWS\system32\\cmd.exe'
            # os.startfile(path)
            os.system('start cmd')

        # playing songs in Ytube
        if 'play' in query:
            query = query.replace('play', '')
            speak('Playing {}'.format(query))
            pywhatkit.playonyt(query)

        # getting ip
        if 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak('Your IP Address is : {}'.format(ip))

        # time
        if 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('The Time is - '+time)

        # wiki

        if 'tell me about' in query:
            person = query.replace('tell me about', '')
            info = wikipedia.summary(person, 1)
            speak(info)

        #opening browsers
        if'open instagram' in query:
            webbrowser.open('www.instagram.com')
        if'open browser' in query:
            speak('What do you want me to search')
            search=recognize()
            speak('Okay')
            webbrowser.open('www.google.com/search?q=' + str(search))

        
        #A simple convo model
        if 'ask me a question' in query:
            speak('Yeah , Sure')
            speak('Are you single')
            query = recognize().lower()
            if 'yes' in query:
                speak('I would say you are no better than waste')
                query = recognize().lower()
                if 'why' in query:
                    speak('It is funny how no one likes you')
                    query = recognize().lower()
                    if 'no' in query:
                        speak("Dont worry, Soon you'll die single")
                        query = recognize().lower()
                        if 'lost' in query:
                            speak('LOL')
            else:
                speak('Dont talk to me!, You cheated me')
                break

        # To stop her
        if 'thank you' in query:
            speak('have a good day, Bye my friend.')
            break

        #To make her learn new phrases and to use them when needed
        else:
            while True:
                #Imma connect the json dict
                with open('words.json') as data:
                    list = json.load(data)
                if query in list:
                    speak(list[query])
                    break
                else:
                    speak('I cant understand...Do you want me to save the phrase?')
                    query = recognize().lower()
                    if 'yes' in query:
                        speak('Repeat the command please')
                        cmd = recognize().lower()
                        speak('What reply should I give')
                        ans = recognize().lower()
                        write(cmd, ans)
                        speak('Thank you for this information')
                        break
                    if 'no' in query:
                        speak('Okay')
                        break
    
        
        

