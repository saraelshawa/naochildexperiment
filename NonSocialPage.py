import Tkinter  as tk
import threading 
from settings import IP_ADDRESS
from settings import PORT
from naoqi import ALProxy
import json
from settings import MOVEMENT_MAPPINGS_FILE_PATH


class NonSocialPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Non social page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        self.textBox = tk.Text(self, height=2, width=10)
        self.textBox.pack()

        with open(MOVEMENT_MAPPINGS_FILE_PATH) as f:
                self.movement_mappings_dict = json.load(f)

        tk.Button(self, text="Retrieve input", command=lambda: self.retrieve_input()).pack()
    
    def retrieve_input(self):
        inputValue=self.textBox.get("1.0", "end-1c")
        print(inputValue)

        log = open(str(inputValue), "r")
        for line in log:
            time = int(line.split(" ")[1])
            behavior = str(line.split(" ")[0])
            print(time)
            print(behavior)
            timer = threading.Timer(int(time), self.run, [str(behavior)]) 
            timer.start() 

        print("Exit\n")



    def run(self, behaviour):
        #if behavior starts with sound 
        # if "sound" in str(behaviour):

        #else
        managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, PORT)
        managerProxy.runBehavior(str(self.movement_mappings_dict[behaviour]))
# 


