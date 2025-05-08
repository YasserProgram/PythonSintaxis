"""
# Ejemplo de bucle for en Python, para iterar sobre un iterable

lista_nombres = ["Yasser", "Yader", "Heler"]
tupla_notas = ("Yasser", 5, 5.8, 4.9)
set_departamentos = {'ventas', "compras", "contabilidad", "producción"}

for nombres in lista_nombres:
    print(nombres)
    
for notas in tupla_notas:
    print(notas)

for departamentos in set_departamentos:
    print(departamentos)
"""    
"""
# Ejemplo de bucle for en Python, para iterar sobre un rango de números,
# para indicar que se repita una acción un número determinado de veces

for _ in range(4):
    print("desde origen avanzar 10 pasos")
    print("girar 90 grados")
"""

"""
# Extraer los indices de un iterable, junto a sus nombres a la vieja antigua

lista_nombres = ["Yasser", "Yader", "Heler"]

for nombre in lista_nombres:
    print(nombre)
    
for indice in range(3): # 3 es la longitud, que tambien pude obtenerla con la funcion len(), len(lista_nombres)
    print(indice, lista_nombres[indice])
"""
"""
# Extraer los indices de un iterable, usando la función enumerate()

lista_nombres = ["Yasser", "Yader", "Heler"]

for indice, nombre in enumerate(lista_nombres):
    print(indice, nombre)
"""