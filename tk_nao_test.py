import Tkinter  as tk
from naoqi import ALProxy    

def fun():
	tts = ALProxy("ALTextToSpeech", "169.254.124.254", 9559)
	tts.say("Hello world!")
	tts.say("I am nao")
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=fun)
slogan.pack(side=tk.LEFT)

root.mainloop()
