from turtle import Turtle, Screen

win = Screen()
win.bgcolor("white")

turtle = Turtle()

turtle.fillcolor('black')

for _ in range(5): 
    turtle.forward(100) 
    turtle.right(144) 

turtle.hideturtle()

win.exitonclick()