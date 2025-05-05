def conectar_bd(**kwargs):
    nombre = kwargs.get("nombre_db", "default")
    user = kwargs["usuario"]
    password = kwargs["password"]
    port = kwargs['port']
    dir_db = kwargs['dir_db']
    
    print(f"Conectando a la base de datos: {nombre}")
    print(f"Login with: {user} - {password}")
    
conectar_bd(nombre_db='Generico', 
            usuario='admin', 
            password='1234', 
            port=5002,
            dir_db = '10.25.47.3',
            query = "SELECT * FROM tabla")
