#pip install PyAudio
#pip install SpeechRecognition
#pip install keyboard

import speech_recognition as sr
import keyboard

while True:
    if keyboard.is_pressed("F12"):
        break
    if keyboard.is_pressed("F6"):
        print("say something ... ")
        r = sr.Recognizer()
        with sr.Microphone() as sound :
            voice = r.listen(sound)
            try:
                keyboard.press("Space")
                say = r.recognize_google(voice)
                keyboard.write(say)
            except:
                pass
