from abc import ABC, abstractmethod

class Pokemon:  
    def __init__(self, nombre, nivel, salud, color):
        self.nombre = nombre 
        self.__nivel = None 
        self.__salud = None
        self.color = color
        
        self.salud = salud # Usar las propiedades definidas al momento de inicializar
        self.nivel = nivel # Usar las propiedades definidas al momento de inicializar
        
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
    
    @property
    def nivel(self):
        return self.__nivel
    
    @nivel.setter
    def nivel(self, nivel):
        if nivel > 0 and nivel <= 100:
            self.__nivel = nivel
        else:
            print("El nivel no puede ser negativo",
                "El nivel no puede ser mayor que 100")