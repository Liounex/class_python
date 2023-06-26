cadena1 = "Hola como estas"
cadena2 = "Mundo"

# devulve una lista de atributos ()
""" resultado  = dir(cadena1) """

# Conviete todo a Mayuscula
""" resultado = cadena1.upper() """

# Convierte a minuscyula
""" resultado = cadena1.lower() """

# Convierte la primera letra en mayuscula
""" resultado = cadena1.capitalize() """

# Busca una cadena en otra cadena
# devulve la posicion si no hay coincidencia devuelve -1
""" resultado = cadena1.find("a") """ # 3
# DEvulve una excepcion en caso no hay coincidencia
""" resultado = cadena1.index("9") """

# Devuelve True si es numerico
""" resultado = cadena1.isnumeric()  """# False
# True si es alfa numerico
# Devulve True si no existe espacios, coma, etc
""" resultado = cadena1.isalpha() """ # False

# Devuelve la cantidad de coincuidencias
""" resultado = cadena1.count("a") """ # 2 , != 0
# Devulve la cantidad de caracteres que tiene
""" resultado = len(cadena1) """

# Si empiza con "X" devulve True
""" resultado = cadena1.startswith("H")  """# True != False

# Si termina con "X" devulve True
""" resultado = cadena1.endswith("s")  """# True != False

# Reemplaza un pedazo de la cadena por otra
""" resultado = cadena1.replace("Hola", "Holas") """ # Hola ==> Holas
        # Encuentra en la cadena    Reemplaza con esto

# Separa las cadenas
resultado = cadena1.split(",")     

print(resultado)