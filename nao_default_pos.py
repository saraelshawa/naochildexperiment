# -*- encoding: UTF-8 -*-
#!/usr/bin/env python
from naoqi       import ALProxy

NAO_IP =  "169.254.186.86"

PORT = 9559

# Proxy for Motion
motionProxy = ALProxy("ALMotion", NAO_IP, PORT)

names = ['LShoulderRoll', 'LShoulderPitch', 'LElbowYaw', 'LElbowRoll','RShoulderRoll', 'RShoulderPitch', 'RElbowYaw', 'RElbowRoll']

default_pos = [-0.30991006,  1.26397407, -1.26405811, -0.53072214,  0.20397997, 1.27326202,  1.21795404,  0.56608796]
motionProxy.setStiffnesses("Body", 1.0)
motionProxy.setAngles(names, default_pos, 0.1)
motionProxy.setStiffnesses("Body", 0.0)


