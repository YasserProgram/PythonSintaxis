# Desarro del juego de la carrera de caracoles con turtle
# Dos tortugas estarán compitiendo en una pista, estos
# van a avanzar aleatoriamente, dependiendo el azar
# puede ganar cualquiera de ellos cuando lleguen a la meta.
# Cuando lleguen a la meta se detendra el bucle

import turtle, random

ventana = turtle.Screen()
ventana.title("Carrera de tortugas")
ventana.bgcolor("gray")
ventana.setup(width=800, height=600)

tortuga1 = turtle.Turtle()
tortuga1.color("blue")
tortuga1.shape("turtle")
tortuga1.penup()
tortuga1.goto(-300,100)



tortuga2 = turtle.Turtle()
tortuga2.color("red")
tortuga2.shape("turtle")
tortuga2.penup()
tortuga2.goto(-300,0)


meta = 300

# Dibujar linea de meta
meta_linea = turtle.Turtle()
meta_linea.penup()
meta_linea.goto(meta,150)
meta_linea.pendown()
meta_linea.goto(meta,-150)
meta_linea.hideturtle()

while True:
    avance_tortuga_1 = random.randint(1, 20)
    avance_tortuga_2 = random.randint(1, 20)
    
    if avance_tortuga_1 % 2 == 0 or avance_tortuga_2 % 2 == 0:
        continue
    
    tortuga1.forward(avance_tortuga_1)
    tortuga2.forward(avance_tortuga_2)  
    
    print(f"El caracol 1 avanza {avance_tortuga_1}")
    print(f"El caracol 2 avanza {avance_tortuga_2}")
    print("---------------------------------------------------------------------")
    
    if tortuga1.xcor() >= meta or tortuga2.xcor() >= meta:
        break
    
if tortuga1.xcor() > tortuga2.xcor():
    print("El caracol 2 ha ganado")
elif tortuga2.xcor() > tortuga1.xcor():
    print("El caracol 2 ha ganado")
else:
    print("Esto es un empate")
    
ventana.mainloop()