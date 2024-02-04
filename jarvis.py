import typing
import pyautogui
import pyttsx3 #converts the entered text into speech.
import speech_recognition as sr
import datetime
import time
import os
import wikipedia
import webbrowser
import random
import sys
import pywhatkit  # pip install pywhatkit. is used for send messages and converting text into handwritten text images.
import pyjokes
# import pyautogui  provides the ability to simulate mouse cursor moves and clicks as well as keyboard button presses.
import requests
import psutil
import instadownloader
import instaloader
from PyQt5 import QtWidgets, QtCore , QtGui
from PyQt5.QtCore import QObject, QTime, QTimer, QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_MainWindow
from translate import Translator
from googletrans import Translator
import distutils_pytest
import pyaudio
import setuptools
import ctypes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[1].id)


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")

    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is: {strTime}")
    
    from translate import Translator

    speak("Hello I'm Jarvis how can i help you")
    
def perform_google_search():
    query = query.replace("Search", "")
    query = query.replace("Search", "")
    query = query.strip()
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def shutdown():
    # Execute the shutdown command
    os.system("shutdown /s /t 1")
def windows_sleep():
    ctypes.windll.powrprof.SetSuspendState(0, 1, 0)

    speak("I'm Uttam Naitam from Nagpur and Studing in DYPatil")
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    def run(self):
        self.TaskExecution()
    

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"user said {self.query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        return self.query


    def TaskExecution(self):
        wishMe()
        while True:

            self.query = self.takecommand().lower()
            if self.query.lower() == "exit":
                speak("Thanks for using me sir, have a good day!")
                break
            elif "search" in self.query.lower() or "google" in self.query.lower():
                perform_google_search(self.query)
            elif "open" in self.query.lower():
                webbrowser.open("http://www.google.com")
            else:
                pass

            if "open notepad" in self.query:
                path="C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2312.18.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
                os.startfile(path)

            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif "open word" in self.query:
                path = "C:\\Program Files\\Microsoft Office 15\\root\\office15\\WINWORD.EXE"
                os.startfile(path)
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            elif 'open google' in self.query:
                webbrowser.open("www.google.com")
            elif 'profile' in self.query:
                webbrowser.open("https://www.linkedin.com/in/uttam-naitam-969397229/")
            elif 'play music' in self.query:
                music_dir = 'C:\\Users\\Uttam\\Desktop\\spotify\\songs' #choose your directory path
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is : {strTime}")
            elif "open vscode" in self.query:
                path = "C:\\Users\\Uttam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #chose your vs code directory path
                os.startfile(path)
           
            elif "close word" in self.query:
                speak("okay sir, closing word application")
                os.system("Taskkill //f //in // WINWORD.EXE")
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down " in self.query:
                shutdown()
            elif "restart the system" in self.query:
                os.system("shutdown /r /t s")

            elif "sleep " in self.query:
                windows_sleep()

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            
            
            elif "instagram profile" in self.query:
                speak("Enter Instagram user name")
                name = input("Enter your Instagram user name:")
                webbrowser.open(f"www.instagra.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                speak("Sier would you like to download profile picture of this accound.")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_onlu=True)
                    speak("I am done sir, profile pictureis saved in our medial folde. now i am ready to do anothe task")
                else:
                    pass

            elif "take screenshot" in self.query:
                speak("Sir, please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak("Please sir hold the screen for few seconds, i am taking screenshot")
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("I am done sir, profile pictureis saved in our medial folder. now i am ready to do another task")
            
            elif " how much battery " in self.query:
                battery = psutil.sensors_battery()
                left_battery = battery.percent
                speak(f"Sir, you have left {left_battery}% battery.")
        
        
startExecution = MainThread() 
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("iron/uttam.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("iron/image.gif")
        self.ui.label_3.setMovie(self.ui.movie)

        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime) 
        timer.start(1000)
        startExecution.start()
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.pushButton_5.setText(label_date)
        self.ui.pushButton_6.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

    
