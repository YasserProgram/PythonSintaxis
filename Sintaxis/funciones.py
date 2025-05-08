def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"La suma entre {numero1} y {numero2} es {resultado}")

def restar(numero1,numero2):
    resultado = numero1 - numero2
    print(f"La resta entre {numero1} y {numero2} es {resultado}")

def multiplicar(numero1,numero2):
    resultado = numero1*numero2
    print(f"La multiplicación entre {numero1} y {numero2} es {resultado}")

def dividir(numero1,numero2):
    resultado = numero1/numero2
    print(f"La división entre {numero1} y {numero2} es {resultado}")
  
# Le pido al usuario que ingrese dos numeros
# y la operacion que desea realizar
continuar = True

while continuar:
    numero1 = int(input("Ingrese su primer número: "))
    numero2 = int(input("Ingrese su segundo número: "))
    operacion = int(input("Elija la operación que desea realizar\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\nElección: "))

    if operacion == 1:
        sumar(numero1,numero2)
    elif operacion == 2:
        restar(numero1,numero2)
    elif operacion == 3: 
        multiplicar(numero1, numero2)
    elif operacion == 4:
        dividir(numero1,numero2)
    else:
        print("Opción no valida. "\
                "Elije una opción entre 1 y 4")
        
    desicion = input("¿Desea continuar? (s/n): ")
    if desicion == "s":
        continuar = True
    elif desicion == "n":
        continuar = False
    else:
        print("Selección no valida")
        break