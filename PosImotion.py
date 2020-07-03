from tkinter import *

win = Tk()
win.title("PosImotion")
win.geometry("700x177")
win.configure(background="light blue")

def show():
    myLabel = Label(win, text=var.get()).pack(side=BOTTOM)

def reset():
    c.deselect()

def close_window():
    win.destroy()
    exit()

var = StringVar()

c = Checkbutton(win, text="Disgust", variable=var, onvalue="Approval, Admiration, Respect", offvalue="")
c.pack(side=LEFT)

c = Checkbutton(win, text="Sadness", variable=var, onvalue="Happiness, Delight, Cheer", offvalue="")
c.pack(side=LEFT)

c = Checkbutton(win, text="Fear", variable=var, onvalue="Faith, Encouragement, Courage", offvalue="")
c.pack(side=LEFT)

c = Checkbutton(win, text="Anger", variable=var, onvalue="Humor, Kindness, Love", offvalue="")
c.pack(side=LEFT)

c = Checkbutton(win, text="Anticipation", variable=var, onvalue="Apprehension, Hope, Joy", offvalue="")
c.pack(side=RIGHT)

c = Checkbutton(win, text="Trust", variable=var, onvalue="Confidence, Faith, Hope", offvalue="")
c.pack(side=RIGHT)

c = Checkbutton(win, text="Joy", variable=var, onvalue="Happiness, Delight, Rejoicing", offvalue="")
c.pack(side=RIGHT)

c = Checkbutton(win, text="Love", variable=var, onvalue="Attachment, Infatuation, Devotion", offvalue="")
c.pack(side=RIGHT)

exitButton = Button(win, text="Exit", command=close_window).pack(side=BOTTOM)

buttonReset = Button(win, text="Reset", command=reset).pack(side=BOTTOM)

confirmButton = Button(win, text="Positivity", command=show).pack(side=BOTTOM)

win.mainloop()
