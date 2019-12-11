from naoqi import ALProxy
from settings import IP_ADDRESS

def sound_1():
    print("in 1")
    tts = ALProxy("ALTextToSpeech", IP_ADDRESS, 9559)
    tts.say("Ow!")

def sound_2():
    print("in 2")

    tts = ALProxy("ALTextToSpeech", IP_ADDRESS, 9559)
    tts.say("Hey!")

def sound_3():
    tts = ALProxy("ALTextToSpeech", IP_ADDRESS, 9559)
    tts.say("Ohh!")

