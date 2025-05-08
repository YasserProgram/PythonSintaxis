condicion_salida = "CONTINUE"

while condicion_salida =="CONTINUE" :
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    mensaje = input("Ingrese el mensaje a enviar: ")
    
    
    print(f"""
          Mensaje enviado a {nombre}
          
          destinatario: {correo}
          
          Mensaje a enviar: {mensaje} 
          """) 
    
    condicion_salida = input("En caso de querer continuar escriba CONTINUE: ")