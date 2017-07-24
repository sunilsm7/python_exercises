import turtle
import tkinter

my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.color('red')
# making circle from Square

def square(length, angle):
    
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)



for i in range(100):
    square(100,90)
    my_turtle.left(11)
    my_turtle.color('blue')
