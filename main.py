import turtle
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(300,300)

pencil = turtle.Turtle()

#1 triangle
pencil.forward(200)

pencil.left(120)
pencil.forward(200)

pencil.left(120)
pencil.forward(200)

#move pencil
pencil.penup()
pencil.right(150)
pencil.forward(100)

#2 triangle start draw
pencil.pendown()
pencil.right(90)
pencil.forward(200)

pencil.right(120)
pencil.forward(200)

pencil.right(120)
pencil.forward(200)

turtle.done()