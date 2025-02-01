import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import openai
import pafy
from bs4 import BeautifulSoup
import requests
import time
import json
import cv2

# Set the PAFY_BACKEND environmental variable to use the internal backend
os.environ["PAFY_BACKEND"] = "internal"

# Initialize the speech engine
engine = pyttsx3.init()

# Set your OpenAI API key
openai.api_key = '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'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
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
        print('Say that again please...')
        return "None"
    return query

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def openApplication(app_name):
    try:
        os.startfile(app_name)
    except Exception as e:
        speak("Sorry, I couldn't open the application.")

def openWebsite(website_name):
    if 'open' in website_name:
        website_name = website_name.replace('open', '').strip()
    webbrowser.open(f"https://{website_name}")

def getYouTubeVideoURL(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for video in soup.find_all('a', href=True):
        if '/watch?v=' in video['href']:
            return f"https://www.youtube.com{video['href']}"
    return None

def playYouTube(video_name):
    if 'on youtube search' in video_name:
        video_name = video_name.replace('on youtube search', '').strip()
    elif 'search' in video_name and 'on youtube' in video_name:
        video_name = video_name.replace('search', '').replace('on youtube', '').strip()
    
    video_url = getYouTubeVideoURL(video_name)
    if video_url:
        webbrowser.open(video_url)
    else:
        speak("Sorry, I couldn't find the video on YouTube.")

def askAI(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    print(answer)
    speak(answer)

def setTimer(duration):
    speak(f"Setting a timer for {duration} seconds.")
    time.sleep(duration)
    speak("Time's up!")

def recordAudio(filename):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Recording audio...")
        audio = r.listen(source)
        with open(filename, "wb") as f:
            f.write(audio.get_wav_data())
        speak("Audio recording saved.")

def recordVideo(filename, duration):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
    start_time = time.time()
    speak("Recording video...")
    while int(time.time() - start_time) < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break
    cap.release()
    out.release()
    speak("Video recording saved.")

def addNote(note):
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    speak("Note added.")

def readNotes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as f:
            notes = f.read()
        speak(notes)
    else:
        speak("No notes found.")

def openFile(filepath):
    try:
        os.startfile(filepath)
    except Exception as e:
        speak("Sorry, I couldn't open the file.")

def greetUser(name):
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak(f"Good morning, {name}!")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon, {name}!")
    else:
        speak(f"Good evening, {name}!")

if __name__ == "__main__":
    speak("Hello, how can I assist you today?")
    speak("What is your name?")
    name_query = takeCommand().lower()
    if 'my name is' in name_query:
        name = name_query.replace('my name is', '').strip()
        greetUser(name)

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'The time is {strTime}')

        elif 'the day' in query:
            tellDay()

        elif 'open' in query:
            openApplication(query.replace('open', '').strip())

        elif 'on youtube search' in query or 'search' in query and 'on youtube' in query:
            playYouTube(query)

        elif 'ask ai about' in query:
            question = query.replace('ask ai about', '')
            askAI(question)

        elif 'open' in query and 'website' in query:
            openWebsite(query)

        elif 'set timer for' in query:
            try:
                duration = int(query.replace('set timer for', '').strip())
                setTimer(duration)
            except ValueError:
                speak("Please specify a valid duration for the timer.")

        elif 'record audio' in query:
            filename = query.replace('record audio', '').strip() + ".wav"
            recordAudio(filename)

        elif 'record video' in query:
            parts = query.replace('record video', '').strip().split()
            if len(parts) == 2 and parts[1].isdigit():
                filename = parts[0] + ".avi"
                duration = int(parts[1])
                recordVideo(filename, duration)
            else:
                speak("Please specify a valid filename and duration for the video recording.")

        elif 'add note' in query:
            note = query.replace('add note', '').strip()
            addNote(note)

        elif 'read notes' in query:
            readNotes()

        elif 'open file' in query:
            filepath = query.replace('open file', '').strip()
            openFile(filepath)

        elif 'weather' in query:
            webbrowser.open('https://www.google.com/search?q=weather')

        elif 'stop' in query or 'end' in query or 'exit' in query:
            speak("Goodbye!")
            break
