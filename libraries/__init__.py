import pyttsx3 
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',145)

def speak(text):
   engine = pyttsx3.init()
   engine.say(text)
   engine.runAndWait()

def setvoiceID(vid):   

   engine = pyttsx3.init()
   
   id=voices[vid].id
   engine.setProperty('voice', id)
   speak('If you want to set this as defualt voice Enter '+str(vid))

def setProperty(voice_id): 
   engine.setProperty('voice', voices[voice_id].id)
   speak("Voice set")

def listenuser():
   r = sr.Recognizer()
   mic=sr.Microphone()
   with mic as source:
      print("speak")
      r.adjust_for_ambient_noise(source)
      input = r.listen(source)
      print("Got Code")
      try:
         processed_text = r.recognize_google(input)
         print(processed_text)
         return processed_text
      except sr.UnknownValueError:
         speak("P-A-I-A cannot recognise your voice")
