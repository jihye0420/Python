import turtle
import random

t=turtle.Turtle()
t.shape("turtle")

def draw_square(x,y,c):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.end_fill()
    return

c=["yellow", "red", "purple", "blue"]
for c in c: 
    draw=draw_square(random.randint(0, 200), random.randint(0, 400), c)

turtle.mainloop()
turtle.bye()
