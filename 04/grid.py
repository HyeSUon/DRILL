import turtle
cnt = 12;
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
while(cnt > 0):
    if(cnt == 6):
        turtle.right(90)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.left(180)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    cnt = cnt-1
turtle.exitonclick()
