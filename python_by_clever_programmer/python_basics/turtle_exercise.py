import turtle
import tkinter

my_turtle = turtle.Turtle()
my_turtle.speed(0)
# making circle from Square

def square(length, angle):
    
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)



for i in range(100):
    square(100,90)
    my_turtle.left(11)
