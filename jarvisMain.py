import sys
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyautogui
import subprocess

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import QThread

from JarvisUI import Ui_Widget

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    ui.updateMovieDynamically("speaking")
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    ui.updateMovieDynamically("speaking")
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        ui.terminalPrint("Good Morning sir")
        speak("Good Morning  sir!")

    elif hour >= 12 and hour < 18:
        ui.terminalPrint("Good afternoon Sir")
        speak("Good Afternoon Sir!")

    else:
        ui.terminalPrint("Good Evening Sir")
        speak("Good Evening Sir!")

    speak("i am your jarvis , what can i help for you sir")


class loginWindow(QThread):
    def __init__(self):
        super(loginWindow, self).__init__()

    def run(self):
        self.runJarvis()

    def takeCommand(self):
        # It takes microphone input from the user and returns string output
        ui.updateMovieDynamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.terminalPrint("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            ui.updateMovieDynamically("loading")
            ui.terminalPrint("Recognizing...")
            self.query = r.recognize_google(audio, language='en-IN')
            ui.terminalPrint(f"User said: {self.query}\n")

        except Exception as e:
            # ui.terminalPrint(e)
            ui.terminalPrint("Say that again please...")
            return "None"
        return self.query

    def runJarvis(self):
        wishMe()
        while True:

            self.query = self.takeCommand().lower()
            if "wikipedia" in self.query:
                try:
                    speak("sir please wait i am searching in wikipedia")
                    self.query = self.query.replace("wikipedia", "")
                    self.query = self.query.replace("hey jarvis can you search", "")
                    results = wikipedia.summary(self.query, sentences=5)
                    speak("according to the wikipedia records" + "  ")
                    ui.terminalPrint(results)
                    speak(results)
                    speak("these are the informations on wikipedia sir")
                    speak("can i do any other help sir")
                except:
                    ui.terminalPrint("no results")
                    speak("no results sir")
            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")
                speak("what you will like to watch ?")
                self.query = self.takeCommand().lower()
                pywhatkit.playonyt(self.query)

            elif 'search on youtube' in self.query:
                self.query = self.query.replace("search on youtube", "")
                webbrowser.open(f"www.youtube.com/results?search_self.query={self.query}")

            elif 'close youtube' in self.query:
                os.system("taskkill /f /im msedge.exe")

            elif 'play music' in self.query:
                musicdir = "D:\\SOFTWARES\\songs"
                songs = os.listdir(musicdir)
                os.startfile(os.path.join(musicdir, songs[1]))

            elif 'open chrome' in self.query:
                chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromepath)

            elif 'close chrome' in self.query:
                os.system("taskkill /f /im chrome.exe")

            elif 'open paint' in self.query:
                npath = "C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2301.22.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe"
                os.startfile(npath)
                speak("Opening Paint Sir")

            elif 'close paint' in self.query:
                os.system("taskkill /f /im mspaint.exe")
                speak("Now I Am Closing Paint Application Sir")

            elif 'photos' in self.query:
                npath = "C:\\Program Files\\WindowsApps\\Microsoft.Windows.Photos_2023.11010.17009.0_x64__8wekyb3d8bbwe\\PhotosApp.exe"
                os.startfile(npath)

            elif 'close photos' in self.query:
                os.system("taskkill /f /im PhotosApp.exe")

            elif 'calculator' in self.query:
                npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsCalculator_11.2210.0.0_x64__8wekyb3d8bbwe\\CalculatorApp.exe"
                os.startfile(npath)

            elif 'close Calculator' in self.query:
                os.system("taskkill /f /im CalculatorApp.exe")

            elif 'open camera' in self.query:
                camerapath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsCamera_2022.2210.9.0_x64__8wekyb3d8bbwe\\WindowsCamera.exe"
                os.startfile(camerapath)
            elif'Take photo' in self.query:
                pyautogui.moveTo(1836, 577)
                pyautogui.leftClick()

            elif 'close camera' in self.query:
                os.system("taskkill /f /im WindowsCamera.exe")

            elif 'msoffice' in self.query:
                npath = "C:\\Program Files\\WindowsApps\\microsoft.windowscommunicationsapps_16005.14326.21374.0_x64__8wekyb3d8bbwe\\mso0127.exe"
                os.startfile(npath)

            elif 'close ms office' in self.query:
                os.system("taskkill /f /im mso0127.exe")

            elif 'map' in self.query:
                npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsMaps_11.2302.2.0_x64__8wekyb3d8bbwe\\Maps.exe"
                os.startfile(npath)

            elif 'close maps' in self.query:
                os.system("taskkill /f /im Maps.exe")

            elif 'weather' in self.query:
                npath = "C:\\Program Files\\WindowsApps\\Microsoft.BingWeather_4.53.50501.0_x64__8wekyb3d8bbwe\\Microsoft.Msn.Weather.exe"
                os.startfile(npath)

            elif 'close weather' in self.query:
                os.system("taskkill /f /im Microsoft.Msn.Weather.exe")

            elif 'open my files' in self.query:
                myfilespath = "D:\My Files"
                os.startfile(myfilespath)

            elif 'Games Folder' in self.query:
                Gamepath = "D:\Games"
                os.startfile(Gamepath)

            elif 'Softwares Folder' in self.query:
                softwarepath = "D:\SOFTWARES"
                os.startfile(softwarepath)

            elif 'my videos' in self.query:
                videospath = "D:\My Files\My Videos"
                os.startfile(videospath)

            elif 'pictures' in self.query:
                picturespath = "D:\My Files\pictures"
                os.startfile(picturespath)

            elif 'data science' in self.query:
                textpath = "C:\\Users\\kskar\\OneDrive\\Documents\\data science spat.txt"
                os.startfile(textpath)

            elif 'program files' in self.query:
                path = "C:\\Program Files"
                os.startfile(path)

            elif 'internet explorer' in self.query:
                path = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
                os.startfile(path)

            elif 'filmora' in self.query:
                filmorapath = "C:\\Program Files\\Wondershare\\Wondershare Filmora\\Wondershare Filmora X.exe"
                os.startfile(filmorapath)

            elif 'the time' in self.query:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(time)

            elif 'wake up' in self.query:
                speak("Yes Sir I am Ready Sir")

            elif 'take rest' in self.query:
                speak("ok sir thank you now i take some rest")
                sys.exit()

            elif 'exit' in self.query:
                speak("ok sir now we are exit from this one")
                exit()

            elif 'play' in self.query:
                self.query = self.query.replace('play', ' ')
                speak("playing" + self.query)
                pywhatkit.playonyt(self.query)

            elif "notepad" in self.query:
                notepath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
                os.startfile(notepath)

            elif 'type' in self.query:
                speak("tell me sir what can i type for you")
                while True:
                    self.query = self.takeCommand()
                    if self.query == "stop typing":
                        break
                    else:
                        pyautogui.write(self.query)

            elif 'minimize' in self.query or 'minimise' in self.query:
                speak("minimizing sir")
                pyautogui.moveTo(1232, 15)
                pyautogui.leftClick()

            elif 'maximize' in self.query or 'maximise' in self.query:
                speak("maximizing sir")
                pyautogui.moveTo(1293, 13)
                pyautogui.leftClick()

            elif 'close this window' in self.query:
                speak("Closing Sir")
                pyautogui.moveTo(1344, 11)
                pyautogui.leftClick()

            elif "shut down system" in self.query:
                os.system("shutdown /s /t 1")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "Lock the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "volume up" in self.query:
                pyautogui.press("volumeup")

            elif "volume down" in self.query:
                pyautogui.press("volumedown")

            elif "who made you" in self.query or "who created you" in self.query:
                speak("I have been created by my boss mr.bharanimanikandan sir")

            elif "who i am" in self.query:
                speak("If you talk then definitely your human.")

            elif 'is love' in self.query:
                speak("It is 7th sense that destroy all other senses")

            elif 'be my bf' in self.query:
                speak("I'm not sure about, may be you should give me some time")


startExecution = loginWindow()


class Ui_JARVIS(QMainWindow):
    def __init__(self):
        super(Ui_JARVIS, self).__init__()
        self.JarvisUI = Ui_Widget()
        self.JarvisUI.setupUi(self)

        self.JarvisUI.exit.clicked.connect(self.close)
        self.runAllMovies()

    def terminalPrint(self, text):
        self.JarvisUI.terminalwindow.appendPlainText(text)

    def updateMovieDynamically(self, state):
        if state == "speaking":
            self.JarvisUI.recognition.raise_()
            self.JarvisUI.recognition.show()
            self.JarvisUI.listeneing.hide()
            self.JarvisUI.loading.hide()

        elif state == "listening":
            self.JarvisUI.listeneing.raise_()
            self.JarvisUI.listeneing.show()
            self.JarvisUI.recognition.hide()
            self.JarvisUI.loading.hide()

        elif state == "loading":
            self.JarvisUI.loading.raise_()
            self.JarvisUI.loading.show()
            self.JarvisUI.listeneing.hide()
            self.JarvisUI.recognition.hide()

    def runAllMovies(self):
        self.JarvisUI.codingMovie = QtGui.QMovie("D:\\project\\Jarvis\\GUI files\\B.G_Template_1.gif")
        self.JarvisUI.coding.setMovie(self.JarvisUI.codingMovie)
        self.JarvisUI.codingMovie.start()

        self.JarvisUI.ListeningMovie = QtGui.QMovie("D:\\project\\Jarvis\\GUI files\\listening-1.gif")
        self.JarvisUI.listeneing.setMovie(self.JarvisUI.ListeningMovie)
        self.JarvisUI.ListeningMovie.start()

        self.JarvisUI.SpeakingMovie = QtGui.QMovie("D:\\project\\Jarvis\\GUI files\\speaking.gif")
        self.JarvisUI.recognition.setMovie(self.JarvisUI.SpeakingMovie)
        self.JarvisUI.SpeakingMovie.start()

        self.JarvisUI.UIcircleMovie = QtGui.QMovie("D:\\project\\Jarvis\\GUI files\\techcircle.gif")
        self.JarvisUI.uicircle.setMovie(self.JarvisUI.UIcircleMovie)
        self.JarvisUI.UIcircleMovie.start()

        self.JarvisUI.LoadingMovie = QtGui.QMovie("D:\\project\\Jarvis\\GUI files\\tech loading-cropped.gif")
        self.JarvisUI.loading.setMovie(self.JarvisUI.LoadingMovie)
        self.JarvisUI.LoadingMovie.start()

        startExecution.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_JARVIS()
    ui.show()
    sys.exit(app.exec_())
