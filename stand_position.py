#~ This script was generated automatically by drang&drop from Position Library
from naoqi import ALProxy

def stand_position():
    print("here")
    try:
        postureProxy = ALProxy("ALRobotPosture", "169.254.186.86", 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ",

    postureProxy.goToPosture("Stand", 0.5)