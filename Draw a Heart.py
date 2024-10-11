from turtle import Turtle, Screen

win = Screen()
win.bgcolor("white")

turtle = Turtle()
turtle.color('red')

turtle.begin_fill() 

turtle.fillcolor("red")
turtle.begin_fill()
turtle.left(140)
turtle.circle(50, 180)
turtle.forward(81)
turtle.left(80)
turtle.forward(81)
turtle.circle(50, 180)

turtle.fillcolor('red') 
turtle.end_fill() 

turtle.hideturtle()
win.exitonclick()