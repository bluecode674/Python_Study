import turtle as tr
import random


for j in range(5):
    for i in range(5):        
        tr.forward(50)
        tr.left(144)
    tr.penup()
    pos_x = random.randint(-300, 300)
    pos_y = random.randint(-300, 300)
    tr.goto(pos_x,pos_y)
    print(tr.position())
    tr.pendown()

tr.done()