import Tkinter  as tk
from naoqi import ALProxy    
from sys import exit
import qi
import time
from settings import IP_ADDRESS


from GazeFollowInteraction import GazeFollowInteraction
from hand_wave import hand_wave
from gangam_style import gangam_style_position, gangam_style_dance
from stand_position import stand_position

# def fun():
	# tts = ALProxy("ALTextToSpeech", "169.254.124.254", 9559)
	# tts.say("Hi, Sho!")
	
def quit():
    global root
    root.quit()


def eye_color():
    session = qi.Session()
    session.connect("tcp://" + IP_ADDRESS + ":9559")
    leds_service = session.service("ALLeds")

    # Example showing how to fade the eyes to green 
    stand_position()
    name = 'FaceLeds'
    intensity = 0.5
    duration = 2.0
    leds_service.fadeRGB(name, "green", duration)
    leds_service.rasta(1)


def moveHead(type, direction, angle, time_end):
    motionProxy = ALProxy("ALMotion", IP_ADDRESS, 9559)

    #left or right
    if type == "HeadYaw":
        if direction == "left":
            angleLists = [[angle]*time_end]
        if direction == "right":
            angleLists = [[-angle]*time_end]
        timeLists = [range(1, time_end+1)]
        print(angleLists, timeLists)
        isAbsolute  = True
        motionProxy.angleInterpolation(["HeadYaw"], angleLists, timeLists, isAbsolute)
    #up or down 
    if type == "HeadPitch":
        if direction == "up":
            angleLists = [[-angle]*time_end]
        if direction == "down":
            angleLists = [[angle]*time_end]
        timeLists = [range(1, time_end+1)]
        isAbsolute  = True
        motionProxy.angleInterpolation(["HeadPitch"], angleLists, timeLists, isAbsolute)


def make_sound():
    #to do 
    stand_position()
    tts = ALProxy("ALTextToSpeech", IP_ADDRESS, 9559)
    tts.say("Ow!")

    leds_service = ALProxy("ALLeds", IP_ADDRESS, 9559)
    leds_service.rasta(1)


gazeFollowInteration = GazeFollowInteraction()
def gaze_follow():
    stand_position()
    next_move = gazeFollowInteration.get_next_move()
    if next_move == GazeFollowInteraction.LEFT_HEAD_MOVE:
        moveHead("HeadYaw", "left", 0.7, 4)
    elif next_move == GazeFollowInteraction.RIGHT_HEAD_MOVE:
        moveHead("HeadYaw", "right", 0.7, 4)
    return


def dance():
    stand_position()
    managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, 9559)
    managerProxy.runBehavior("gangnamstyle1234-91e48b/GangnamStyle")


    # aup = ALProxy("ALAudioPlayer", "169.254.124.254", 9559)
    # fileId = aup.loadFile("/home/sara/repos/testing_nao/file_example_WAV_1MG.wav")
    # time.sleep(5)
    # aup.play(fileId)

def hand_wave_func():
    stand_position()
    managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, 9559)
    managerProxy.runBehavior("animations/Stand/Gestures/Hey_1")
    # tts = ALProxy("ALAnimationPlayer", IP_ADDRESS, 9559)
    # tts.run("animations/Stand/Gestures/Hey_1!")


def changeAngles(name, add_angle):
    print("in change angles")
    motionProxy = ALProxy("ALMotion", IP_ADDRESS, 9559)

    useSensors    = True
    commandAngle = motionProxy.getAngles(name, useSensors)
    
    new_pos = [commandAngle[0] + add_angle]
    motionProxy.angleInterpolationWithSpeed([name], new_pos, 0.1)

    # motionProxy.setAngles(name, new_pos, 0.1)
    # motionProxy.setStiffnesses("Body", 1.0)


root = tk.Tk()
root.geometry("500x500")
frame = tk.Frame(root)
frame.pack()
root.protocol('WM_DELETE_WINDOW', root.quit())



button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.LEFT)

eye_button = tk.Button(frame, text="Eyes", fg="red", command=eye_color)
eye_button.pack(side=tk.LEFT)

sound_button = tk.Button(frame, text="Bring Attention", fg="red", command=make_sound)
sound_button.pack(side=tk.LEFT)

gaze_following_button = tk.Button(frame, text="Gaze Follow", fg="blue", command=gaze_follow)
gaze_following_button.pack(side=tk.LEFT)

play_dance_button = tk.Button(frame, text="Dance", fg="blue", command=dance)
play_dance_button.pack(side=tk.LEFT)

wave_hand_button = tk.Button(frame, text="Wave hand", fg="blue", command=hand_wave_func)
wave_hand_button.pack(side=tk.LEFT)


def leftKey(event):
    print "Left key pressed"
    # moveHead("HeadYaw", "left", 0.2, 2)
    changeAngles("HeadYaw", 0.3)


def rightKey(event):
    print "Right key pressed"
    changeAngles("HeadYaw", -0.3)
    # moveHead("HeadYaw", "right", 0.2, 2)

def upKey(event):
    print "Up key pressed"
    moveHead("HeadPitch", "up", 0.2, 2)

def downKey(event):
    print "Down key pressed"
    moveHead("HeadPitch", "down", 0.2, 2)

root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)


root.mainloop()

def get_behaviours():
    alBehaviorManagerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, 9559)
    names = alBehaviorManagerProxy.getInstalledBehaviors()
    print "Behaviours installed on the robot:"
    print names
    
    print ("\n Behaviours running on the robot")
    allItems = alBehaviorManagerProxy.getRunningBehaviors()
    for i in allItems:
        print i

