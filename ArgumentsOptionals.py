# Crear una función que calcule el precio final de un producto
# en función de si tiene o no, un descuento

def calcular_precio(nombre_producto, cantidad, precio_u, descuento=0):
    precio_final = (cantidad * precio_u)*(1-descuento)
    print(f"El precio final para {nombre_producto}es {precio_final}")
    
calcular_precio("Camila", 2, 20)
calcular_precio("Camila", 2, 20, 0.20) 
 