"""
def sumar(n1, n2):
    resultado = n1+n2
    return resultado

resultado = sumar(5, 10)
resultado_final = resultado * 2
print(f"El resultado es {resultado_final}")
"""

"""
#Multiples return
def calcular_precio(nombre_producto, precio_unitario, cantidad, descuento=0):
    precio_final = (precio_unitario * cantidad) *(1-descuento)   
    return nombre_producto, cantidad, precio_final #Retorna una tupla

#compra_final = calcular_precio("camisa", 100, 2, 0.1)
#print(compra_final)

nombre, cantidad, precio = calcular_precio("camisa", 100, 2, 0.1) # Desempaquetado de tupla
print(nombre)
print(cantidad)
print(precio)
"""