import turtle

def copo_de_nieve_koch(tortuga, orden, tamaño):
    if orden == 0:
        tortuga.forward(tamaño)
    else:
        for ángulo in [60, -120, 60, 0]:
            copo_de_nieve_koch(tortuga, orden-1, tamaño/3)
            tortuga.left(ángulo)

# Configuración inicial
ventana = turtle.Screen()
ventana.bgcolor("cyan") 
ventana.title("Copo de nieve")

tortuga_koch = turtle.Turtle()
tortuga_koch.penup()
tortuga_koch.goto(-150, 90)
tortuga_koch.pendown()
tortuga_koch.speed(0)

# Dibuja el copo de nieve de KochS
for _ in range(3):
    copo_de_nieve_koch(tortuga_koch, 4, 300)
    tortuga_koch.right(120)

# Cierra la ventana al hacer clic
ventana.exitonclick()
