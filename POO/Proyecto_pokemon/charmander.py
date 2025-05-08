from tipofuego import TipoFuego
class Charmander(TipoFuego):
    def __init__(self, nombre, nivel, salud, 
                 temperatura_max, color):
        
        super().__init__(nombre, nivel, salud, 
                         temperatura_max, color)

charmander_1 = Charmander('Chori',140,100,1200,'Naranja')
print(charmander_1.atacar())