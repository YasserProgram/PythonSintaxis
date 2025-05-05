edad = int(input("Ingrese su edad: "))

#Opcion 1
"""
if edad >=18:
    mensaje = "Usted es mayor de edad"
else:
    mensaje = "Usted es menor de edad"
"""

#Opcion 2: Operador ternario
mensaje = "Usted es mayor de edad" if edad >= 18 else "Usted es menor de edad"
print(mensaje)