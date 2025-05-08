"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#def retornar_pares(numero):
#    return numero%2 == 0

#lista_pares = list(filter(retornar_pares, numbers))
lista_pares = list(filter(lambda x: x%2 == 0, numbers))# Esto me retorna un objeto filter
print(lista_pares)
"""
"""
names = ["Mario", "Luigi", "Peach", "Topad", "Yoshi"]

#def retornar_nombres_a(nombre):
#    return nombre[0] == "A"

#lista_nombres_a = list(filter(retornar_nombres_a, names))
lista_nombres_a = list(filter(lambda x:x[0] == "A", names))

print(lista_nombres_a)
"""