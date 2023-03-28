import turtle

# Configuración de la ventana
ventana = turtle.Screen()
ventana.bgcolor("white")

# Configuración de la pluma
pluma = turtle.Turtle()
pluma.shape("turtle")
pluma.color("red", "purple")
pluma.pensize(3)

# Dibujar el corazón
pluma.begin_fill()
pluma.left(45)
pluma.forward(100)
pluma.circle(50, 180)
pluma.right(90)
pluma.circle(50, 180)
pluma.forward(100)
pluma.end_fill()

####

# Configuración de la pluma
pluma = turtle.Turtle()
pluma.shape("turtle")
pluma.color("red", "pink")
pluma.pensize(3)

# Dibujar el corazón
pluma.begin_fill()
pluma.left(45)
pluma.forward(100/1.2)
pluma.circle(50/1.2, 180)
pluma.right(90)
pluma.circle(50/1.2, 180)
pluma.forward(100/1.2)
pluma.end_fill()

#####

# Configuración de la pluma
pluma = turtle.Turtle()
pluma.shape("turtle")
pluma.color("red", "purple")
pluma.pensize(3)

# Dibujar el corazón
pluma.begin_fill()
pluma.left(45)
pluma.forward(100/1.5)
pluma.circle(50/1.5, 180)
pluma.right(90)
pluma.circle(50/1.5, 180)
pluma.forward(100/1.5)
pluma.end_fill()

####

# Configuración de la pluma
pluma = turtle.Turtle()
pluma.shape("turtle")
pluma.color("red", "pink")
pluma.pensize(3)

# Dibujar el corazón
pluma.begin_fill()
pluma.left(45)
pluma.forward(100/1.8)
pluma.circle(50/1.8, 180)
pluma.right(90)
pluma.circle(50/1.8, 180)
pluma.forward(100/1.8)
pluma.end_fill()


# Salir al hacer clic en la ventana
ventana.exitonclick()
