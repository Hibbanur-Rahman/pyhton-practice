import turtle
turtle.bgcolor("light pink")
turtle.pensize(2.5)
turtle.speed(0.5)
color=["red","blue","green","yellow"]
for x in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(120)
        turtle.left(10)

turtle.mainloop()