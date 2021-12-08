# # EnlargeShrinkCircle.py

# from tkinter import *


# class EnlargeShrinkCircle:
#  def __init__(self):
#   self.radius = 50

#   window = Tk()

#   self.canvas = Canvas(window, bg="white", width=200, height=200)
#   self.canvas.pack()
#   self.canvas.create_oval(
#       100 - self.radius, 100 - self.radius,
#       100 + self.radius, 100 + self.radius,
#       tags="oval")

#   self.canvas.bind("<button-1>", self.increaseCircle)
#   self.canvas.bind("<button-3>", self.decreaseCircle)

#   window.mainloop()

#  def increaseCircle(self, event):
#   self.canvas.delete("oval")
#   if self.radius < 100:
#    self.radius += 2
#   self.canvas.create_oval(
#       100 - self.radius, 100 - self.radius,
#       100 + self.radius,
#       100 + self.radius, tags="oval")

#  def decreaseCircle(self, event):
#   self.canvas.delete("oval")
#   if self.radius > 2:
#    self.radius -= 2
#   self.canvas.create_oval(
#       100 - self.radius,
#       100 - self.radius,
#       100 + self.radius,
#       100 + self.radius,
#       tags="oval")


# EnlargeShrinkCircle()


from tkinter import *
Width=600
Height=600
w=200
h=200
window = Tk()

def callbackUP(event):
    canvas.delete("all")
    global w
    global h
    w=w+10
    h=h+10
    canvas.create_rectangle(50, 50, w, h)


def callbackDOWN(event):
    canvas.delete("all")
    global w
    global h
    w=w-10
    h=h-10
    canvas.create_rectangle(50, 50, w, h)

canvas=Canvas(window, width=Width, height=Height, bg="white")
canvas.pack()
canvas.create_rectangle(50, 50, w, h)

frame=Frame(window)
frame.pack()
canvas.bind("<Button-1>", callbackUP)
canvas.bind("<Button-3>", callbackDOWN)

window.mainloop()
