# -*- encoding: UTF-8 -*-
#!/usr/bin/env python
from naoqi import ALProxy
import csv
import numpy as np
import time

NAO_IP = "169.254.124.254"
PORT = 9559

# Proxy for Motion
motionProxy = ALProxy("ALMotion", NAO_IP, PORT)

names = ['LShoulderRoll', 'LShoulderPitch', 'LElbowYaw', 'LElbowRoll','RShoulderRoll', 'RShoulderPitch', 'RElbowYaw', 'RElbowRoll']


def reset_default_pose():
    #default_pos = [-0.30991006,  1.26397407, -1.26405811, -0.53072214,  0.20397997, 1.27326202,  1.21795404,  0.56608796]
    default_pos = [-0.31415927,  1.28391612, -1.28399992, -0.47089601,  0.28067994, 1.27479601,  1.23943007,  0.46331]
    motionProxy.setStiffnesses("Body", 1.0)
    time.sleep(0.1)
    motionProxy.setAngles(names, default_pos, 0.6)
    print("ok")


def play_from_csv(filename, timesteps = 90, sleep_factor = 0):
    f = open(filename)
    reader = csv.reader(f, lineterminator='\n')
    motors = np.zeros((timesteps,8))

    i=0                                                                                                                                
    for row in reader:                                                  
        motors[i,:] = [float(x) for x in row][0:8]#np.float32(row[0:8])
        i+=1

    # we cannot move it anymore
    motionProxy.setStiffnesses("Body", 1.0)
    fractionMaxSpeed = 0.8

    names = ['LShoulderRoll', 'LShoulderPitch', 'LElbowYaw', 'LElbowRoll','RShoulderRoll', 'RShoulderPitch', 'RElbowYaw', 'RElbowRoll', 'HeadYaw']

    for k in range(timesteps):
        motionProxy.setAngles(names, motors[k,:].tolist(), fractionMaxSpeed)
        print(k)
        time.sleep(0.5)
    return motors
