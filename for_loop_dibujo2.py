import turtle

ventana = turtle.Screen() 
ventana.bgcolor("white") 
tortuga = turtle.Turtle() 
tortuga.speed(1)

#Dibujar una estrella
for _ in range(5):
    tortuga.forward(250) 
    tortuga.right(144) 

ventana.exitonclick() # Espera a que el usuario haga clic en la ventana para cerrarla
