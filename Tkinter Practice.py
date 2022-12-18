import turtle
import random

Screen = turtle.getscreen()
Screen.bgcolor("yellow")

Bob = turtle.Turtle()
Colors = ["red","green","cyan","blue","purple","orange","black"]
Bob.speed(10)

for i in range(5):

    Bob.color(Colors[random.randint(0,6)],Colors[random.randint(0,6)])
    Bob.begin_fill()
    Bob.circle(10)
    Bob.end_fill()
    Bob.color(Colors[random.randint(0,6)],Colors[random.randint(0,6)])
    Bob.begin_fill()
    Bob.circle(-10)
    Bob.end_fill()
    Bob.color(Colors[random.randint(0,6)],Colors[random.randint(0,6)])
    Bob.left(90)
    Bob.begin_fill()
    Bob.circle(10)
    Bob.end_fill()
    Bob.color(Colors[random.randint(0,6)],Colors[random.randint(0,6)])
    Bob.begin_fill()
    Bob.circle(-10)
    Bob.end_fill()

    Bob.color(Colors[random.randint(0,6)],"green")
    Bob.forward(300)
    Bob.left(126.7)
    Bob.end_fill()






turtle.mainloop()
