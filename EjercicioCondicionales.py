# Desarrollar un script que pida la edad y la altura del usuario
# Si la persona e smayor de edad puede participar
# Pero la persona debe medir mas de 170 cm
# Si la persona no mide 170 cm podra participar si es mayor a 25 años
# y si la altura es mayor a 165 cm

edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura en cm: "))

#Opcion 1
"""
if (edad >= 18 and altura > 170) or (edad > 25 and altura > 165):
    print("Puede participar")
else:
    print("No puede participar")
"""
    
# Opcion 2
"""
if edad >= 18:
    if (altura >= 170) or (edad >= 25 and altura >= 165):
        print("Puede participar")
    else:
        print("No puede participar")
else:
    print("Debes ser mayor de edad para participar")
"""