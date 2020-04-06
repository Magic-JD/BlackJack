from tkinter import *
from tkinter.ttk import Frame, Button, Style


class View(Tk):

    def __init__(self):
        super().__init__()
        self.configure(background='green')
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.title("Welcome to Blackjack app")
        self.geometry("{}x{}".format(w, h))

        lbl = Label(self, text="Hello")

        lbl.grid(column=1, row=0)

        btn = Button(self, text="Click Me")

        btn.grid(column=0, row=10)
        btn2 = Button(self, text="Click Me harder")

        btn2.grid(column=0, row=5)
        self.mainloop()
