import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(
    'C:\\Program Files\\Mozilla Firefox\\firefox.exe'))
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak('I am Jarves! Please tell me how may i help you?')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    f = open("pass.txt", "r")
    if f.mode == 'r':
        server.ehlo()
        server.starttls()
        server.login('roshanstark007@gmail.com', f.read())
        server.sendmail('roshanstark007@gmail.com', to, content)
    server.close()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognising....')
        query = r.recognize_google(audio, language='en-uk')
        print(f'User-said: {query}\n')

    except Exception as e:
        print(e)
        print('Say that again please!!')
        return 'None'
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching in Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(f"According to Wikipedia {results}")

        elif 'hello' in query:
            print("Hello There!!")
            speak('hello there mister Tired Warrior')

        elif 'youtube' in query:
            # webbrowser.open('youtube.com')
            print('Opening YouTube.....')
            speak('opening youtube')
            webbrowser.get('firefox').open('youtube.com')

        elif 'gmail' in query:
            print('Let me show you!!')
            speak('Let me show you!!')
            webbrowser.get('firefox').open('mail.google.com')

        elif 'stackoverflow' in query:
            print('Taking you to StackOverflow...')
            speak('Taking you to StackOverflow...')
            webbrowser.get('firefox').open('stackoverflow.com')

        elif 'terminal' in query:
            print('Getting you your terminal!!')
            speak('Getting you your terminal!!')
            os.startfile('C:\\Windows\\system32\\cmd.exe')

        elif 'browser' in query:
            print('Opening Firefox for you!')
            speak('Opening Firefox for you!')
            os.startfile(
                'C:\\Program Files\\Mozilla Firefox\\firefox.exe')

        elif 'code' in query:
            print('Opening your favourite Editor!!!')
            speak('Opening your favourite Editor!!!')
            os.startfile('D:\\Microsoft VS Code\\Code.exe')

        elif 'thank you' in query:
            print('Your Welcome!!')
            speak('Your Welcome!!')

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {time}")
            speak(f"The time is {time}")

        elif 'email' in query:
            try:
                speak("Can you type his emailid for me?")
                to = input("Can you type his emailid for me?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Your email has been sent.")
            except Exception as e:
                print(e)
                speak(
                    'I\'m sorry i am not able to send the email. Are you sure what you typed was right?')

        elif 'quit' or 'exit' or 'stop' in query:
            try:
                print("Exiting....")
                speak("Exiting....")
                exit()
            except Exception as e:
                print(e)
                speak('I\'m sorry i am not able to send the email. Are you sure what you typed was right?')

        else:
            speak('I\'m sorry i am not able to send the email. Are you sure what you typed was right?')
