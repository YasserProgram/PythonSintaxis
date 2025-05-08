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
        
    def atacar(self): 
        print(f"Pikachu ataca y genera {self.__nivel/4} de daño")
        
pikachu_1 = Pikachu("Yasser", 100, 100, 6, 2, "Amarillo")
print(f"El Pikachu llamado {pikachu_1.nombre} tiene un nivel" \
      f"{pikachu_1.nivel} y es de tipo {pikachu_1.tipo}.")

"""
pikachu_1.nivel = -120 
Aqui tendriamos un problema, bien es cierto que el nivel
puede cambiar porque si Pikachu entrena o evoluciona
puede aumentar su nivel, pero no puede ser negativo, es decir,
este atributo sie puede cambiar, pero no puede ser negativo.

pikachu_1.tipo = "Fuego" 
Sin encapsulamiento, esto podria ser posible, pero no tiene sentido
ya que Pikachu es de tipo electrico, y por mucho que entrene
no deberia poder cambiar su tipo. Por tanto, este atributo
debe ser inmutable, que el usuario no pueda acceder a el para
cambiarlo.

Por defecto todos los atributos de una clase son publicos, es decir,
que se pueden acceder desde fuera de la clase, pero si queremos que
un atributo no se pueda modificar, tenemos que definirlo como privado.
Para ello, tenemos que ponerle dos guiones bajos al principio del nombre

¿Que problemas resuelve el encapsulamiento?
1. Evitar que el usuario pueda modificar atributos que no
se deberian modificar, como el tipo de Pikachu.
2. Evitar que los atributos que se pueden modificar, como el nivel,
sean modificados de forma incorrecta, como que el nivel sea negativo.
3. Atributos que no deberian verse. Por ejemplo, el voltaje y amperaje maximo
de Pikachu, no deberian verse desde fuera de la clase. Pues no quiero
exponerlo a las demas clases, ya que no es necesario y puede que 
afecte el funcionamiento de la clase, en el caso del amperaje y voltaje
revelaria caracteristicas de Pikachu que no deberian ser reveladas, ya
que podrían sacar ventaja de esto"""