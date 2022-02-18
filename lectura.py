import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('voice', 'spanish')
engine.setProperty('volume', 1)


# Sólo es una función de texto a voz
def saySomething(somethingToSay):
    engine.say(somethingToSay)
    engine.runAndWait()


while True:
    something = input("Algo para decir: ")
    print("Presta atención, sube el volúmen..")
    saySomething(something)