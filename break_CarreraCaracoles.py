# Desarro del juego de la carrera de caracoles
# Dos tortugas estarán compitiendo en una pista, estos
# van a avanzar aleatoriamente, dependiendo el azar
# puede ganar cualquiera de ellos cuando lleguen a la meta.
# Cuando lleguen a la meta se detendra el bucle

import random

meta = 20
caracol1 = 0
caracol2 = 0

"""
while caracol1 < meta and caracol2 < meta:
    # Avance del caracol 1
    avance_caracol_1 = random.randint(1, 4)
    avance_caracol_2 = random.randint(1, 4)
    
    caracol1 += avance_caracol_1
    caracol2 += avance_caracol_2
    
    print(f"El caracol 1 avanza {avance_caracol_1}, para un total de {caracol1}")
    print(f"El caracol 2 avanza {avance_caracol_2}, para un total de {caracol2}")
    print("---------------------------------------------------------------------")

if caracol1 > caracol2:
    print("El caracol 2 ha ganado")
elif caracol2 > caracol1:
    print("El caracol 2 ha ganado")
else:
    print("Esto es un empate")
"""

while True:
    # Avance del caracol 1
    avance_caracol_1 = random.randint(1, 4)
    avance_caracol_2 = random.randint(1, 4)
    
    caracol1 += avance_caracol_1
    caracol2 += avance_caracol_2
    
    print(f"El caracol 1 avanza {avance_caracol_1}, para un total de {caracol1}")
    print(f"El caracol 2 avanza {avance_caracol_2}, para un total de {caracol2}")
    print("---------------------------------------------------------------------")

    if caracol1 >= meta or caracol2 >= meta:
        break
    
if caracol1 > caracol2:
    print("El caracol 2 ha ganado")
elif caracol2 > caracol1:
    print("El caracol 2 ha ganado")
else:
    print("Esto es un empate")