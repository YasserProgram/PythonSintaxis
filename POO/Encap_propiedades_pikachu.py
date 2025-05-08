class Pikachu:
    __tipo = 'Electrico'
    
    def __init__(self, nombre, nivel, salud, voltaje_max,
                 amperaje_max, color):
        
        self.nombre = nombre 
        self.__nivel = nivel 
        self.__salud = salud 
        self.__voltaje_max = voltaje_max
        self.__amperaje_max = amperaje_max
        self.color = color
        
    @property
    def salud(self): #Recomendación, ponerle el mismo nombre al atributo y al método
        return self.__salud
    
    @salud.setter
    def salud(self, salud):
        if salud > 0 and salud <= 100:
            self.__salud = salud
        else:
            print("La salud no puede ser negativa",
                "La salud no puede ser mayor que 100")
    
    """ Esta es la manera de Java   
    def get_salud(self):
        return self.__salud
    
    def set_salud(self, salud):
        if salud > 0 and salud <= 100:
            self.__salud = salud
        else:
            print("La salud no puede ser negativa",
                "La salud no puede ser mayor que 100")
    """
    
    def atacar(self): 
        print(f"Pikachu ataca y genera {self.__nivel/4} de daño")
        
pikachu_1 = Pikachu("Yasser", 100, 100, 6, 2, "Amarillo")

#pikachu_1.__tipo = "Fuego" # No se puede
pikachu_1.salud = 50
salud_pikachu_1 = pikachu_1.salud

print(f"El Pikachu llamado {pikachu_1.nombre} tiene una salud de {salud_pikachu_1}.")


"""La maneera de Java
salud_pikachu_1 = pikachu_1.get_salud() # Ahora si se puede acceder a la salud
pikachu_1.set_salud(50) # Cambiamos la salud de Pikachu

print(f"El Pikachu llamado {pikachu_1.nombre} tiene una salud de {salud_pikachu_1}.")
"""