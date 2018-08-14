from turtle import*
from random import randint
def draw_square(length, square_color):
    speed(-1)
    color(square_color)
    for i in range(4):
        forward(length)
        left(90)
    mainloop()
draw_square(randint(100,200),"yellow")