import random
from tkinter import *
Width=600
Height=600
number=random.randint(6, 20)

window = Tk()

canvas=Canvas(window, width=Width, height=Height, bg="white")

def rec():
    x1=random.randint(0, 200)
    y1=random.randint(0, 200)
    x2=random.randint(40, 500)
    y2=random.randint(40, 500)
    color=["red", "orange", "yellow", "green", "blue", "violet", "black"]
    fill_color= random.choice(color)

    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
    canvas.pack()


for item in range(number):    
    rec()
frame=Frame(window)
frame.pack()
window.mainloop()
