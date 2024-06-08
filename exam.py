from tkinter import *
import random

window = Tk()

def change_text():
    button.configure(text="변경")


def show():
    print(e.get())

photo1 = PhotoImage(file="cat.gif")
label = Label(window, image=photo1)
button = Button(window, text="클릭", command=show)
e = Entry(window)

label.grid(row= 1, column=0 )

button.grid(row =0, column =1)
e.grid(row=0, column= 0)



window.mainloop()