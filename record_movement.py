# -*- encoding: UTF-8 -*-
#!/usr/bin/env python
from naoqi import ALProxy
import vision_definitions
from PIL import Image
import operator
import numpy as np
import cv2
import csv

import pathlib2
import os
import datetime
import time

import matplotlib.pyplot as plt

now = datetime.datetime.now()
save_dir = str(now.hour) + "-" + str(now.minute) + "_" + str(now.microsecond) + "_" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "_" 
pathlib2.Path(save_dir).mkdir(parents=True, exist_ok=True)

NAO_IP = "169.254.124.254"
PORT = 9559

motionProxy = ALProxy("ALMotion", NAO_IP, PORT)



csv_2darray=[]
csv_2darray_raw = []
time_steps = 90
for k in range(time_steps):
#################################################################### Get joint Angles

    # Example that finds the difference between the command and sensed angles.
    #names         = "Body"
    names         = ['LShoulderRoll', 'LShoulderPitch', 'LElbowYaw', 'LElbowRoll','RShoulderRoll', 'RShoulderPitch', 'RElbowYaw', 'RElbowRoll', 'HeadYaw']
    useSensors    = False
    commandAngles = motionProxy.getAngles(names, useSensors)

    useSensors  = True
    sensorAngles = motionProxy.getAngles(names, useSensors)

    errors = []
    for i in range(0, len(commandAngles)):
        errors.append(commandAngles[i]-sensorAngles[i])
    print "Errors"
    print errors

    time.sleep(0.1)
    #################################################################### Preprocessing Joint data

    # min_values=[-0.3142,-2.0857,-2.0857,-1.5446,-1.3265,-2.0857,-2.0857,0.0349, 0.0349]
    # size_values=[0.3142+1.3265,2.0857+2.0857,2.0857+2.0857,1.5446-0.0349,0.3142+1.3265,2.0857+2.0857,2.0857+2.0857,1.5446-0.0349, 1.5446-0.0349] 
    # substracted_values=map(operator.sub, sensorAngles, min_values)
    # normal_joints=map(operator.truediv, substracted_values, size_values)
    # print names
    # print normal_joints



    ################################################################### CSV Formatted data

    # csv_list=normal_joints
    # csv_2darray.append(csv_list)
    csv_list_raw = sensorAngles
    csv_2darray_raw.append(csv_list_raw)

    ################################################################### Save CSV


# f = open(os.path.join(save_dir, 'nao_data.csv'), 'w')
# writer = csv.writer(f, lineterminator='\n')
# writer.writerows(csv_2darray)



f = open(os.path.join(save_dir, 'nao_data_raw.csv'), 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerows(csv_2darray_raw)

f.close()






# plt.figure()
# plt.subplot(311)
# for i in range(1, 4):
#     plt.plot(np.arange(time_steps), [bla[i] for bla in csv_2darray])
# plt.title("Left arm")

# plt.subplot(312)
# for i in range(4,8):
#     plt.plot(np.arange(time_steps), [bla[i] for bla in csv_2darray])
# plt.title("Right arm")





