import Tkinter  as tk
from naoqi import ALProxy    
from sys import exit
print("here here")
def fun():
	tts = ALProxy("ALTextToSpeech", "169.254.124.254", 9559)
	tts.say("Hello world!")
	tts.say("I am nao")
root = tk.Tk()
root.geometry("500x500")
frame = tk.Frame(root)
frame.pack()

def quit():
    global root
    root.quit()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=fun)
slogan.pack(side=tk.LEFT)
print("here")
root.mainloop()
