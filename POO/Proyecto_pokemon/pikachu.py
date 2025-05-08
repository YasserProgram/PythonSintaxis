from tipoelectrico import TipoElectrico

class Pikachu(TipoElectrico):
    # Este init es de la clase Pikachu
    def __init__(self, nombre, nivel, salud, voltaje_max,
                 amperaje_max, color, longitud_cola): #Este metodo(su cuerpo) se ejecuta en bien se crea el objeto/instancia de esta clase
        # Se le pasa los atributos a la clase padre, al inicializar la clase Pikachu, se inicializa la clase padre TipoElectrico 
        super().__init__(nombre=nombre, nivel=nivel,
                         salud=salud, color=color, 
                         voltaje_max=voltaje_max,
                         amperaje_max=amperaje_max) # La ejecución lo que hace es ejecutar el inicializador de la clase padre, lo sabemos por el super

        self.__longitud_cola = None
        
        self.longitud_cola = longitud_cola # Usar las propiedades definidas al momento de inicializar
    
    # Se recomienda que el setter y el getter tengan el mismo nombre
    # Recomendación, ponerle el mismo nombre al atributo y al método
        
    @property # Para crear el getter
    def longitud_cola(self):
        return self.__longitud_cola
    
    @longitud_cola.setter # Para crear el setter
    def longitud_cola(self, longitud_cola):
        if longitud_cola > 0:
            self.__longitud_cola = longitud_cola
        else:
            print("La longitud de la cola no puede ser negativa")  
            
    def atacar_cola_hierro(self):
        print(f"Ataca con cola de hierro y genera {self.longitud_cola/0.5} de daño")
    
if __name__ == '__nmain__': #Esto es si se ejecuta el archivo directamente, no si se importa
    pikachu_1 = Pikachu("Yasser", 100, 100, 6, 2, "Amarillo", 1)
    pikachu_1.salud = 50

    pikachu_1.atacar()
    pikachu_1.atacar_cola_hierro()