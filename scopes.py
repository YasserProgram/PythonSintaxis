#Scope global
"""
nombre = "Yasser"

def imprimir_nombre():
    #global nombre
    nombre = "Carlos"
    print(f"Hola como estas {nombre}?")
    
imprimir_nombre()
print(f"El valor de mi variable global es {nombre}")
"""

#Scope local
"""
def imprimir_nombre():
    local = "Yasser"
    print(f"Hola como estas {local}?")
    
imprimir_nombre()
print(f"Hola {local} como estas?")
"""

#Scope enclusing
"""
def imprimir_nombre():
    nombre_local = "Yasser"
    edad_local = 23
    print(f"Hola {nombre_local} como estas? y su edad {edad_local} años")
    
    def imprimir_edad():
        nonlocal edad_local
        edad_local = 24
        print(f"Su edad es {edad_local} años")
        
    imprimir_edad()
    print(f"Su edad es {edad_local} años")
imprimir_nombre()
"""