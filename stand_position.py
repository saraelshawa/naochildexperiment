#~ This script was generated automatically by drang&drop from Position Library
from naoqi import ALProxy
from settings import IP_ADDRESS
def stand_position():
    try:
        postureProxy = ALProxy("ALRobotPosture", IP_ADDRESS, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ",

    postureProxy.goToPosture("Stand", 0.1)