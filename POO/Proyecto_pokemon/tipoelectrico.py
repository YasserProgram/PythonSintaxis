from pokemon import Pokemon

class TipoElectrico(Pokemon):
    
    __tipo = "Electrico"
    
    def __init__(self, nombre, nivel, salud, voltaje_max,
                 amperaje_max, color):
        
        super().__init__(nombre=nombre, nivel=nivel,
                         salud=salud, color=color)
        
        self.__voltaje_max = None
        self.__amperaje_max = None
        
        self.amperaje_max = amperaje_max # Usar las propiedades definidas al momento de inicializar
        self.voltaje_max = voltaje_max # Usar las propiedades definidas al momento de inicializar
        
        
    @property
    def voltaje_max(self):
        return self.__voltaje_max
    
    @voltaje_max.setter
    def voltaje_max(self, voltaje_max):
        if voltaje_max > 0 and voltaje_max <= 100:
            self.__voltaje_max = voltaje_max
        else:
            print("El voltaje no puede ser negativo")
            
    @property
    def amperaje_max(self):
        return self.__amperaje_max

    @amperaje_max.setter
    def amperaje_max(self, amperaje_max):
        if amperaje_max > 0 and amperaje_max <= 100:
            self.__amperaje_max = amperaje_max
        else:
            print("El amperaje no puede ser negativo")
    
    def atacar(self): 
        print(f"Ataca con electricidad y genera {(self.voltaje_max + self.amperaje_max)/4} de daño") #Siempre accediendo a la propiedad, accder directamente al atributo estaria prohibido
