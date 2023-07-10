import speech_recognition as sr
import pyttsx3
import pywhatkit as pw
import datetime
import wikipedia
#import pyjokes <- would be fun but pyttsx3 uses your OS default language and in russian its scuffed LOL
listening = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1])
#something that alexa will do after hearing 'alexa'
def talk(text):
    engine.say(text)
    engine.runAndWait()
def wait_command():
    try:
        with sr.Microphone() as source:
            print('Tell me your deepest secrets...')
            voice = listening.listen(source)
            command = listening.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:    
        pass
    return command

def run_alexa():
    command = wait_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pw.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is '+ time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    #elif 'joke' in command: talk(pyjokes.get_joke())    
    else: 
        talk('Please say command again.')

while True:
    run_alexa()