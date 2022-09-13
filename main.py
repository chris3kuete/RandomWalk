import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")


# my_colors = ["blue", "yellow", "green", "black", "dark gray", "red", "purple", "pink"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b) #creates a tupple
    return rand_color


angles = [0, 90, 160, 250]
tim.speed("normal")

for _ in range(100):
    tim.pensize(10)
    tim.color(random_color())
    tim.forward(35)
    tim.setheading(random.choice(angles))
