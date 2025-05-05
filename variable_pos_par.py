
#Parametros posicionales variables

def suma(*args):
    print(type(args))  # Imprime el tipo de args, que es una tupla
    return sum(args)

"""
def suma(*args):
    resultado = 0
    for number in args:
        resultado += number
    return resultado
"""
 
resultado = suma(5, 10, 6, 7, 2, 3, 4, 1, 8, 9)
print(f"El resultado es {resultado}")