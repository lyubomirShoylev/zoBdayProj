# from tkinter import *

# class MyDialog:

#     def __init__(self, parent):

#         top = self.top = Toplevel(parent)

#         Label(top, text="Value").pack()

#         self.e = Entry(top)
#         self.e.pack(padx=5)

#         b = Button(top, text="OK", command=self.ok)
#         b.pack(pady=5)

#     def ok(self):

#         print("value is", self.e.get())

#         self.top.destroy()


# root = Tk()
# Button(root, text="Hello!").pack()
# root.update()

# d = MyDialog(root)

# root.wait_window(d.top)
# from tkinter import *
# import time

# gui = Tk()

# var=IntVar()

# gui.geometry("800x800")

# c = Canvas(gui ,width=800 ,height=800)

# c.pack()

# oval = c.create_oval(5,5,60,60,fill='pink')
# # oval = c.create_oval(5,5,10,10)

# a = 5

# b = 5

# for x in range(0 ,100):

#   c.move(oval,a,b)

#   c.update()
#   time.sleep(.03)

# gui.title("First title")

# gui.mainloop()
# ra


# import winsound

# print("hello")
# winsound.Beep(400, 2000)

from tkinter import Tk
import tkinter.font
Tk()
for name in sorted(tkinter.font.families()):
    print(name)