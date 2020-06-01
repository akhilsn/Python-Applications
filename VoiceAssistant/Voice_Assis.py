# Import Libraries

# Pyttsx3 is an offline cross-platform Test-to-Speech library which is compatible with both Python 3
# and supports multiple TTS engines
import pyttsx3
import datetime
import wikipedia
import os
import random
import webbrowser as wb
import speech_recognition as sr


engine = pyttsx3.init('sapi5')  # The Speech Application Programming Interface or SAPI is an API developed by Microsoft to allow
                                # the use of speech recognition and speech synthesis within Windows applications

voices = engine.getProperty('voices')
# From this Microsoft API, my computer already supports 2 voices: Male (DAVID) and Female(Zira).
# print(voices[0].id)        #-> prints David
# print(voices[1].id)        #-> prints Zira

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

#--------------------------------------------------------------------------------------------------------------------

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#--------------------------------------------------------------------------------------------------------------------

def wishMe():
    '''
    This function wishes the creator, according to the current time.
    '''

    hour = int(datetime.datetime.now().hour)        # this will store the current hour (0-24) in the var. hour
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir. Hope you are enjoying the beautiful day today')
    elif(hour >= 12 and hour < 16):
        speak(' Good After Noon Sir. Hope you have done your lunch')
    elif(hour > 16 and hour < 24 ):
        speak('Good Evening Sir. Hope you had a good day so far.')

    speak('I am Jarvis. Please tell me how I may help you!')

#--------------------------------------------------------------------------------------------------------------------

def takeCommand():
    '''
    Takes command from the Microphone input from the user, and return string output
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print('Can you say that again please...')
        return 'None'

    return query

#--------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing Tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening Youtube.com Sir')
            wb.open('www.youtube.com')

        elif 'open google' in query:
            speak('Opening Google.com Sir')
            wb.open('www.google.com')

        elif 'open worldometer' in query:
            speak('Opening Worldometer Sir')
            wb.open('https://www.worldometers.info/coronavirus/')

        # elif 'play music' in query:
        #     speak('Playing music')
        #     musicdir = ''
        #     songs = os.listdir(musicdir)
        #     i = random.randrange(0, len(songs) - 1)
        #     os.startfile(os.path.join(musicdir, songs[i]))

        elif 'the time' in query:
            speak('Let me check what the time is Sir')
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is: {strtime}\n')

        elif 'open pycharm' in query:
            speak('Opening Pyvharm Sir')
            pycharm_path = "C:\Program Files\JetBrains\PyCharm Community Edition 2020.1\bin\pycharm64.exe"
            os.startfile(pycharm_path)

        elif 'quit jarvis' in query:
            speak('Thank you Sir.')
            break


# Can be further added with more functionalities such as playing music, opening files ...
#--------------------------------------------------------------------------------------------------------------------