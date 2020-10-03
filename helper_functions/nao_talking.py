from naoqi import ALProxy
from settings import IP_ADDRESS
from settings import PORT
tts = ALProxy("ALTextToSpeech", IP_ADDRESS, PORT)
tts.say("Hello, world!")
