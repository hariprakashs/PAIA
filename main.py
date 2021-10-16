#Welcome to PAIA - Personal Artifical Intelligent Assitant
from libraries import listenuser, setProperty, setvoiceID,speak
import libraries
class User:
    def __init__(self,user):
        self.user=user
        file=open("libraries/bin/usernames.txt","a")
        file.write(user+'\n')
        speak(user)
    def getDefaultvoice(self):

        for i in range(2):
            setvoiceID(i)
    
    def listen(self):
        listenuser()
        
    def set_property(self,set):
        setProperty(set)

    def greet(self):
        speak("welcome "+ self.user + " \t to  P  A  I  A   which  means \t Personal \t Artificial \t Intelligent \t Assistant")
        speak("Lets start Fresh!")


print("Welcome to PAIA")
speak("Welcome to PAIA")
print("Please Enter you name")
speak("Please Enter you name")
user_name=input()
user=User(user_name)
user.getDefaultvoice()
set=int(input())
user.set_property(set)

user.greet()
user.listen()

