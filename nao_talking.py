from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "169.254.124.254", 9559)
tts.say("Hello, world!")
