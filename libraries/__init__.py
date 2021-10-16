import pyttsx3 
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
