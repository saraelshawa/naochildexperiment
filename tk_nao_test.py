import Tkinter  as tk
from naoqi import ALProxy    
from sys import exit
def fun():
	tts = ALProxy("ALTextToSpeech", "169.254.124.254", 9559)
	tts.say("Hi!")
	tts.say("I am nao")

def quit():
    global root
    root.quit()

def moveHead(type, direction):
    motionProxy = ALProxy("ALMotion", "169.254.124.254", 9559)

    #left or right
    if type == "HeadYaw":
        angleLists = [[0.1, 0.5]]
        timeLists = [[1.0, 2.0]]
        isAbsolute  = True
        motionProxy.angleInterpolation(["HeadYaw"], angleLists, timeLists, isAbsolute)
    #up or down 
    # if type == "HeadPitch":
    #     break

root = tk.Tk()
root.geometry("500x500")
frame = tk.Frame(root)
frame.pack()



button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame, text="Hello", command=fun)
slogan.pack(side=tk.LEFT)


def leftKey(event):
    print "Left key pressed"
    moveHead("HeadYaw", "bla")

def rightKey(event):
    print "Right key pressed"

def upKey(event):
    print "Up key pressed"

def downKey(event):
    print "Down key pressed"

root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)


print("here")
root.mainloop()
