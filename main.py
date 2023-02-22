import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb


minion=pyttsx3.init()
voice=minion.getProperty('voices')
minion.setProperty('voice', voice[1].id)

def speak(audio):
    print('MINION: ' +audio)
    minion.say(audio)
    minion.runAndWait()
def time():
    Time = datetime.datetime.now().strftime('%I:%M:%p')
    speak('Now '+Time)
def welcome():
    hour = datetime.datetime.now().hour
    time()
    if hour>=6 and hour<12:
        speak('Good morning, boss !')
    elif hour>=12 and hour<18:
        speak('Good afternoon, boss !')
    elif hour>=18 and hour<24:
        speak('Good night, boss !')
    speak('How can i help you ?')
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=1
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print('Me: '+query)
    except sr.UnknownValueError:
        print('Sorry sir! I did not get that! Typing the command ')
        query=str(input('Your oder is: '))
    return query
    
if __name__ =="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak('What search, boss ?')
            search=command().lower()
            url=f"https://www.google.com.vn/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')          
        elif "youtube" in query:
            speak('What search ?')
            search=command().lower()
            url=f"https://www.youtube.com/results?search_query={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "facebook" in query:
            """ speak('What search ?')
            search=command().lower() """
            url=f"https://www.facebook.com/"
            wb.get().open(url)
            speak(f'Here is facebook')
        elif "quit" or 'close' in query:
            speak("Minion is off. Goodbye boss")
            quit()