import turtle

ventana = turtle.Screen() 
ventana.bgcolor("white") 
tortuga = turtle.Turtle() 
tortuga.speed(1)

#Dibujar un cuadrado
"""
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
"""

for _ in range(4):
    tortuga.forward(100) 
    tortuga.right(90) 

ventana.exitonclick() # Espera a que el usuario haga clic en la ventana para cerrarla
