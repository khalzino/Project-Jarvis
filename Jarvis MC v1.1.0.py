#Mic Version

import webbrowser
import speech_recognition as sp
from datetime import datetime
import pyttsx3
import time
import os
import random
import sys

rec = sp.Recognizer()
jarvis = pyttsx3.init()
now = datetime.now()
current_time = now.strftime("%H:%M")
voices = jarvis.getProperty('voices')
myMicro = sp.Microphone(device_index=1)

print("What is your name")
jarvis.say("b, what is your name")
jarvis.runAndWait()
name = input(": ")
os.system("clear")

print("Hi, I'm Jarvis, your virtual assistant\nHow Can i help you")
jarvis.say("Hi, I'm Jarvis, your virtual assistant, how can i help you")
jarvis.runAndWait()

while True:
    os.system("cls")
    with myMicro as source:
        print(name+", Im Listening...")
        audio = rec.listen(source)
        ci = rec.recognize_google(audio)

        if ci == "tell me a joke" or ci == "tell me a joke":
            jokemaker = [
            "I got million joke to tell you",
            "Trust me this is going to make you laugh",
            "Ok Jarvis joke mode is on",
        ]
            jokemaker2 = random.choice(jokemaker)
            print("\n"+jokemaker2)
            jarvis.say("bim, "+jokemaker2)
            time.sleep(0.4)

            actualjoke = [
                "What’s the smartest insect? A spelling bee!",
                "How does the ocean say hi? It waves!",
                "Name the kind of tree you can hold in your hand? A palm tree!",
                "Where did the music teacher leave her keys? In the piano!",
                ]

            actualjoke2 = random.choice(actualjoke)
            print(actualjoke2)
            jarvis.say(actualjoke2)
            jarvis.runAndWait()
    

        elif ci == "good" or ci == "im fine":
            print("well thats good to know")
            jarvis.say("b, Well thats good to know")
            jarvis.runAndWait()
        
        elif ci == "are you alright":
            print("Im Fine, Thanks For Asking")
            jarvis.say("Im Fine, Thanks for Asking")
            jarvis.runAndWait()
        
        elif ci == "open google" or ci == "open google.com":
            print("Opening Now")
            jarvis.say("b, opening now")
            jarvis.runAndWait()
            webbrowser.open_new("https://www.google.com")

        elif ci == "open a website":
            print("Please write the URL below")
            jarvis.say("please write the url below")
            jarvis.runAndWait()
            url = input("Enter Here: ")
            os.system("cls")
            print("Opening Now")
            jarvis.say("opening now")
            jarvis.runAndWait()
            webbrowser.open_new(url)

        elif ci == "how are you" or ci == "How are you":
            treat = [
                "Hello, I'm fine thanks",
                "I'm pretty good, thanks",
                "I'm happy to be here",
                "I'm Good, what about you",
            ]
            treat2 = random.choice(treat)
            print(treat2)
            jarvis.say(treat2)
            jarvis.runAndWait()
    
        elif ci == "time" or ci == "what is the time" or ci== "what time is it":
            print("The Time now in your region is ", current_time)
            jarvis.say("The Time now in your region is ", current_time)
            jarvis.runAndWait()

        elif ci == "what is your name" or ci == "who are you":
            print("My Name Is J.A.R.V.I.S but but i shortened it to Jarvis")
            jarvis.say("My Name Is Jarvis but but i shortened it to That")
            jarvis.runAndWait()
        
        elif ci == "how old are you" or ci == "what is your age":
            print("Im afraid i dont have an age")
            jarvis.say("Im afraid i dont have an age")
            jarvis.runAndWait()

        elif ci == "nice":
            print("Well, Good to know")
            jarvis.say("Well, Good to know")
            jarvis.runAndWait()

        elif ci == "hey jarvis":
            hj = [
                "I'm here",
                "Go Ahead...",
                "Hello how can i help",
                "Is there anything that i can do for you",
            ]
            hj2 = random.choice(hj)
            print(hj2)
            jarvis.say("b, "+hj2)
            jarvis.runAndWait()
    
        elif ci == "":
            print("Please say something valid")
            jarvis.say(", Please say something valid")
            jarvis.runAndWait()

        elif ci == "order products from amazon" or ci == "order products from ebay":
            print("This Feture is Coming Soon")
            jarvis.say("This Feture is Coming Soon")
            jarvis.runAndWait()
    
        elif ci == "hi" or ci == "Hi" or ci == "Hello" or ci == "hello":
            greet = [
                "Go Ahead",
                "Hi",
                "Im here",
                "Jarvis here. Let me know if i can help",
            ]
            greet2 = random.choice(greet)
            print(greet2)
            jarvis.say("b, "+greet2)
            jarvis.runAndWait()
        
        elif ci == "rename" or ci == "change my name":
            print("What Do you want to change it into")
            jarvis.say("What Do you want to change it into")
            jarvis.runAndWait()
            name = input("Write Here: ")
            os.system("cls")
            print("Your name is now changed!")
            jarvis.say("Your name is now changed!")
            jarvis.runAndWait()


        else:
            idk = [
                "Im not sure if I Understand?",
                "I did not get that correctly?",
                "I dont know what that means?",
            ]   
            idk2 = random.choice(idk)
            print(idk2)
            jarvis.say(idk2)
            jarvis.runAndWait()