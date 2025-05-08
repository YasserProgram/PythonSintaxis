from abc import ABC, abstractmethod

class Pokemon(ABC):  
    # Este init es de la clase Pokemon
    def __init__(self, nombre, nivel, salud, color):
        self.nombre = nombre 
        self.__nivel = None 
        self.__salud = None
        self.color = color
        
        self.salud = salud # Usar las propiedades definidas al momento de inicializar
        self.nivel = nivel # Usar las propiedades definidas al momento de inicializar
        
    # Se recomienda que el setter y el getter tengan el mismo nombre
    # Recomendación, ponerle el mismo nombre al atributo y al método
    
    @property # Para crear el getter
    def salud(self): # Recomendación, ponerle el mismo nombre al atributo y al método (Ej:salud)
        return self.__salud
    
    @salud.setter # Para crear el setter
    def salud(self, salud):
        if salud > 0 and salud <= 100:
            self.__salud = salud
        else:
            print("La salud no puede ser negativa",
                "La salud no puede ser mayor que 100")
    
    @property # Para crear el getter
    def nivel(self):
        return self.__nivel
    
    @nivel.setter # Para crear el setter
    def nivel(self, nivel):
        if nivel > 0:
            self.__nivel = nivel
        else:
            print("El nivel no puede ser negativo",
                "El nivel no puede ser mayor que 100")
            
    @abstractmethod        
    def atacar(self):
        pass