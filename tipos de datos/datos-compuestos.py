# Lista
# agrupa datos
lista = ["Hola", "Mundo", True, 100, 1.85]
print(lista)
# devuelve la posicion del elemento
print(lista[0])
# modificando la posicion de un elementi
lista[1] = "¿Como estas?"
print(lista)

# Tuplas
# caracteristicas =|
# no se pueden modificar
tupla = ("Hola", "Mundo", True, 100, 1.85)
# Genera error ==> tupla[0] = "Python"

# Conjunto set
# caracteristicas =|
# Se puede redefinir,
# no se puede modificar,
# no se puede acceder por el indece del elemento,
# no permite la repeticion de un elemento
conjunto = {"Hola", "Mundo", True, 100, 1.85}

# Diccionario
diccionario = {
    'nombre': "Lucas",
    'edad': 21,
    'altura': 1.84
}
print(diccionario)
# se accede por la clave (key) clave : valor
print(diccionario['nombre'])
