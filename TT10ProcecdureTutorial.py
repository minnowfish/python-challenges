import turtle

def triangle_draw(x,y,sz):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(60) 
    turtle.pendown()
    for i in range(3):
        turtle.forward(sz)
        turtle.right(120)

        


for y in range (-500,500,100):
    for x in range (-800,800,100):
        triangle_draw(x,y,50)
turtle.done()
