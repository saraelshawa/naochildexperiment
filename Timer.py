import Tkinter as tk
import time
# https://stackoverflow.com/questions/45551179/how-do-i-implement-start-stop-and-reset-features-on-a-tkinter-countdown-timer

class TimerApp(tk.Frame):
    def __init__(self, limit, onEnd, master=None, **kw):
        tk.Frame.__init__(self, master=master, **kw)
        self.paused = False
        self.limit = limit
        self.current = 0
        self.onEnd = onEnd
        self.createWidgets()
        self.countdown(0)
    
    def createWidgets(self):
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()

        self.start_button = tk.Button(self, text="RESUME", fg="red", command=self.startTime)
        self.start_button.pack()
        
        self.pause_button = tk.Button(self, text="PAUSE", fg="red", command=self.pauseTime)
        self.pause_button.pack()
        
        self.reset_button = tk.Button(self, text="RESET", fg="red", command=self.resetTime)
        self.reset_button.pack()
        
    def startTime(self):
        #Resume Time
        print("resume button clicked")
        self.paused = False
        self.countdown(self.current)

    
    def pauseTime(self):
        print("pause button clicked")
        self.paused = True

    def resetTime(self):
        print("reset button clicked")
        self.paused = True
        self.current = 0
        self.countdown(0)

    def returnCurrentTime(self):
        return self.current
        

    def countdown(self, current = None):
        if current is not None:
            self.current = current

        if self.paused:
            print("paused")
            self.label.configure(text="Paused: %s" % time.strftime('%M:%S', time.gmtime(self.current)))
            return

        if self.current >= self.limit:
            self.label.configure(text="time's up!")
            print("calling gaze following")
            self.onEnd()
            return 

        else:
            self.label.configure(text="Timer: %s" % time.strftime('%M:%S', time.gmtime(self.current)))
            # print(time.gmtime(self.current))
            self.current = self.current + 1
            self.after(1000, self.countdown)

# if __name__ == "__main__":
#     app = TimerApp(5)
#     app.mainloop()