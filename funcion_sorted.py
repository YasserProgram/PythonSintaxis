estudiantes = [
    ('Yasser', 24, 5, '555-1234'),
    ('Yader', 23, 5, '555-5678'),
    ('Yasmin', 22, 4, '555-5879'),
]

#def ordenar_por_edad(estudiante):
#    return estudiante[1]

#lista_Estudaintes_edad = sorted(estudiantes, key=ordenar_por_edad)
lista_Estudaintes_edad = sorted(estudiantes, key=lambda x:x[1])
print(lista_Estudaintes_edad)