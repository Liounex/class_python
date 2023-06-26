# variables con enteros 'int'
a = 5
b = 8
c = a + b
print(c)

# variables con cadena de texto 'string'
nombre = "Hola"
# modicando variables comunes
nombre = "Mundo"
nombre = "Python"
print(nombre)

# funciona con enteros 'int'
numero = 10
numero += 1  # hace la suma con el valor de 'numero'
# y el valor despues del igual '='
numero += 5
print(numero)

# concatenacion de variables con +
name = "Juan"
welcome = "Hola" + name + "¿Como estas?"
print(welcome)

# concatenacion de variables con f-strings
# toma un dato y lo convierte a texto
name = "Juan"
welcome = f"Hola {name} ¿Como estas?"
# Borrar datos alojados en memoria
# --> del welcome
print(welcome)

# busqueda de datos en variables es
# case sensitive 'operacion de pertenencia'
# devuelven un booleano (True o False)
print("ola" not in welcome)
print("ola" in welcome)

# Este es un comentario no interpretado
# por el lenguaje

# formas de declarar una variable
# camelCase ==> nombreCompelto = ""
# recomendacion de python
# snake_case = nombre_completo = ""
