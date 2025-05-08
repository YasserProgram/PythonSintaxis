from pokemon import Pokemon

class TipoFuego(Pokemon):
    
    __tipo = "Fuego"
     
    def __init__(self, nombre, nivel, salud,
                 temperatura_max, color):
        
        super().__init__(nombre=nombre, nivel=nivel,
                         salud=salud, color=color)
        
        self.__temperatura_max = None
     
        self.temperatura_max = temperatura_max # Usar las propiedades definidas al momento de inicializar

    # Se recomienda que el setter y el getter tengan el mismo nombre
    # Recomendación, ponerle el mismo nombre al atributo y al método
    
    @property # Para crear el getter
    def temperatura_max(self):
        return self.__temperatura_max

    @temperatura_max.setter # Para crear el setter
    def temperatura_max(self, temperatura_max):
        if temperatura_max > 0:
            self.__temperatura_max = temperatura_max
        else:
            print("La temperatura no puede ser negativa")
            
    def atacar(self):
        print(f'Ataque con fuego y genera {self.temperatura_max*0.5} de daño')
    