import turtle
message = input("What would you like me to write?")
turtle.write(message)
turtle.forward((len(message)+2)*3.7)
turtle.shape("turtle")

turtle.done()
