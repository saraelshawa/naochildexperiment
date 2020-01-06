import Tkinter  as tk
# from StartPage import StartPage

class NonSocialPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Non social page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        self.textBox = tk.Text(self, height=2, width=10)
        self.textBox.pack()

        tk.Button(self, text="Retrieve input", command=lambda: self.retrieve_input()).pack()
    
    def retrieve_input(self):
        inputValue=self.textBox.get("1.0", "end-1c")
        print(inputValue)




