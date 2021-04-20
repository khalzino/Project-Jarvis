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

print("Hi, I'm Jarvis, your virtual assistant\nHow Can i help you")
jarvis.say("Hi, I'm Jarvis, your virtual assistant, how can i help you")
jarvis.runAndWait()

while True:
    os.system("cls")
    with myMicro as source:
        print("Im Listening...")
        audio = rec.listen(source)
        toText = rec.recognize_google(audio)

        if toText == "tell me a joke" or toText == "tell me a joke":
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
    

        elif toText == "good" or toText == "im fine":
            print("well thats good to know")
            jarvis.say("b, Well thats good to know")
            jarvis.runAndWait()
        
        elif toText == "are you alright":
            print("Im Fine, Thanks For Asking")
            jarvis.say("Im Fine, Thanks for Asking")
            jarvis.runAndWait()

        elif toText == "how are you" or toText == "How are you":
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
    
        elif toText == "time" or toText == "what is the time" or toText == "what time is it":
            print("The Time now in your region is ", current_time)
            jarvis.say("The Time now in your region is ", current_time)
            jarvis.runAndWait()

        elif toText == "what is your name" or toText == "who are you":
            print("My Name Is J.A.R.V.I.S but but i shortened it to Jarvis")
            jarvis.say("My Name Is Jarvis but but i shortened it to That")
            jarvis.runAndWait()
        #
        elif toText == "how old are you" or toText == "what is your age":
            print("Im afraid i dont have an age")
            jarvis.say("Im afraid i dont have an age")
            jarvis.runAndWait()

        elif toText == "nice":
            print("Well, Good to know")
            jarvis.say("Well, Good to know")
            jarvis.runAndWait()

        elif toText == "hey jarvis":
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
    
        elif toText == "":
            print("Please write something valid")
            jarvis.say(", Please write something valid")
            jarvis.runAndWait()

        elif toText == "order products from amazon" or toText == "order products from ebay":
            print("This Feture is Coming Soon")
            jarvis.say("This Feture is Coming Soon")
            jarvis.runAndWait()
    
        elif toText == "hi" or toText == "Hi" or toText == "Hello" or toText == "hello":
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