# Tengo una lista de números enteros, y
# solo debo imprimir los numeros pares

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
for numero in lista_numeros:
    if numero % 2 == 0:
        print(numero)
"""
for numero in lista_numeros:
    if numero % 2 !=0:
        continue
    print(numero)
    
    