# from tkinter import *
# from tkinter import ttk

# Width = 500
# Height = 300

# x = 100
# y = 100
# x2=200
# y2=200


# def left():
#     canvas.delete("all")
#     global x
#     global y
#     global x2
#     global y2
#     x = x-10
#     x2 = x2-10
#     canvas.create_rectangle(x, y, x2, y2, fill="red")

# def right():
#     canvas.delete("all")
#     global x
#     global y
#     global x2
#     global y2
#     x = x+10
#     x2 = x2+10
#     canvas.create_rectangle(x, y, x2, y2, fill="red")

# def up():
#     canvas.delete("all")
#     global x
#     global y
#     global x2
#     global y2
#     y = y-10
#     y2 = y2-10
#     canvas.create_rectangle(x, y, x2, y2, fill="red")


# def down():
#     canvas.delete("all")
#     global x
#     global y
#     global x2
#     global y2
#     y = y+10
#     y2 = y2+10
#     canvas.create_rectangle(x, y, x2, y2, fill="red")


# window = Tk()

# canvas = Canvas(window, width=Width, height=Height, bg="white")
# canvas.pack()
# canvas.create_rectangle(x, y, x2, y2, fill="red")
# frame = Frame(window)
# frame.pack()

# btleft = ttk.Button(frame, text="<-(left)", command=left).grid(row=1, column=0)
# btright = ttk.Button(frame, text="->(right)", command=right).grid(row=1, column=2)
# btup = ttk.Button(frame, text="^(up)", command=up).grid(row=1, column=4)
# btdown = ttk.Button(frame, text="v(down)", command=down).grid(row=1, column=6)


# window.mainloop()


from tkinter import *
from tkinter import ttk
window = Tk()


ttk.Label(window, text = "Text1", bg="blue").grid(row = 0, column = 0)
ttk.Label(window, text = "Text2", bg="green").grid(row = 1, column = 1)
ttk.Label(window, text = "Text3", bg="red").grid(row = 2, column = 2)


window.mainloop()

