"""
#Convertir a mayoscula

lista_nombres = ["mario", "luigi", "peach", "topad", "yoshi"]

lista_nombre_mayus = map(str.upper, lista_nombres) # Esto me retorna un objeto map

print(list(lista_nombre_mayus)) # por lo tanto debo hacer el casteo a tipo lista
"""
"""
#Agregar un sufijo
lista_frutas = ["manzana", "pera", "uva", "sandia", "melon"]
sufix = "_fruta"

#def agregar_sufijo(fruta):
#    return fruta + sufix 

#lista_frutas_sufix = list(map(agregar_sufijo, lista_frutas)) 
lista_frutas_sufix = list(map(lambda x:x+sufix, lista_frutas)) 
print(lista_frutas_sufix)
"""