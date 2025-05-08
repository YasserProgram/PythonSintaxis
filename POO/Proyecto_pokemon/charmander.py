from tipofuego import TipoFuego
class Charmander(TipoFuego):
    def __init__(self, nombre, nivel, salud, 
                 temperatura_max, color):
        
        super().__init__(nombre=nombre, nivel=nivel, salud=salud, 
                         temperatura_max=temperatura_max, color=color)

if __name__ == '__main__': # Esto es si se ejecuta el archivo directamente, no si se importa
    charmander_1 = Charmander('Chori',140,100,1200,'Naranja')
    print(charmander_1.nivel)