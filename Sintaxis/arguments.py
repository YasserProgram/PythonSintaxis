def imprimir_nombre(primer_nombre,
                    segundo_nombre,
                    primer_apellido,
                    segundo_apellido):
    print(f"Hola {primer_nombre} {segundo_nombre}"\
          f" {primer_apellido} {segundo_apellido}"\
              " Bienvenid@ al curso de python")
    
    
#Positional arguments 
#imprimir_nombre("Yasser", "Smith", "Torres", "Guzman")

#Keyword arguments
"""
imprimir_nombre(primer_apellido="Torres",
                    segundo_nombre="Smith",
                    segundo_apellido="Guzman",
                    primer_nombre="Yasser",)

imprimir_nombre("Yasser", "Smith", 
                segundo_apellido="Guzman", 
                primer_apellido="Torres")
"""

# Iterable unpacking
"""
estudiantes = ("Yasser", "Smith", "Torres", "Guzman")
imprimir_nombre(*estudiantes)
"""

#Dictionary unpacking
"""
estudiante_dict = {
    "primer_nombre": "Yasser",
    "segundo_nombre": "Smith",
    "primer_apellido": "Torres",
    "segundo_apellido": "Guzman"
}

imprimir_nombre(**estudiante_dict)
"""