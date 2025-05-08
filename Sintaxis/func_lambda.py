"""
#Ordenar las listas
def retornar_nota(estudiante): #Función que accede(retorna) a la nota de los estudiantes
    return estudiante[1]

#lambda argumento: retorno -> lambda estudiante: estudiante[1]
lambda x: x[1] # Función que accede(retorna) la nota de cada estudiante
"""

lista_estudiantes = [("Yasser", 5), 
                     ("Yader", 4), 
                     ("Heler", 4.5), 
                     ("Yas", 4.8), 
                     ("Yasminita", 4.9)]

#lista_ordenada = sorted(lista_estudiantes,key=retornar_nota, reverse=True) #Usando una función normal 
lista_ordenada = sorted(lista_estudiantes,key=lambda x:x[1], reverse=True) #Usando una función anonima
print(lista_ordenada)

 #Practica de funciones lambda, almacenandolas en variables

"""
ista = [1,2,3]

retorno = lambda x:x[1]

print(retorno(ista))



sumar = lambda numero1, numero2: numero1 + numero2
print(sumar(2,3))

"""