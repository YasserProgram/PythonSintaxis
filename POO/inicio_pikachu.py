class Pikachu:
    tipo = 'Electrico' #Atributos de clase
    
    def __init__(self, nombre, nivel, salud):
        self.nombre = nombre #Atributos de instancia
        self.nivel = nivel #Atributos de instancia
        self.salud = salud #Atributos de instancia
    
    def atacar(self): 
        print(f"Pikachu ataca y genera {self.nivel/4} de daño")
    
pikachu_1 = Pikachu("Yasser", 100, 100) 
pikachu_2 = Pikachu("Yader", 120, 1000) 

print(F"El Pikachu llamado {pikachu_1.nombre} ataca.")
pikachu_1.atacar()

print(F"El Pikachu llamado {pikachu_2.nombre} ataca.")
pikachu_2 .atacar()
2
 