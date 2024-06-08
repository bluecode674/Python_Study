from tkinter import *



window = Tk()
p1 = PhotoImage(file="img.gif")
w = Label(window, image=p1)
w.p1 = p1
w.pack()
l1=Label(window, text="오래된 영화")
l1.pack()
e1 = Entry(window)
e1.pack()
b1 = Button(window, text="sumbit")
b1.pack()

window.mainloop()