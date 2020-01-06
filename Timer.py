import Tkinter as tk
import time 
class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(60)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining >= 100:
            self.label.configure(text="time's up!")
        else:
            
            # self.label.configure(text="Timer: %d" % self.remaining)
            self.label.configure(text="Timer: %s" % time.strftime('%M:%S', time.gmtime(remaining)))
            print(time.gmtime(self.remaining))
            self.remaining = self.remaining + 1
            self.after(1000, self.countdown)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()