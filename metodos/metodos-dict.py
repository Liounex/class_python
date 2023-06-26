diccionario = {
    "nombre": 'Juan',
    "apellido": 'Vargas',
    "edad": 34 
}

#devulve las claves (tambien sirve para iterar)
""" claves = diccionario.keys() """

# Devulve el valor de la clave escrita (clave:valor)
# ('nombre' : 'Juan')
# si no existe muestra none y no lanza excepcion
""" claves = diccionario.get('nombre') """ # ==> Juan

# Elimina todos los elemntos del diccionario
""" diccionario.clear() """

# Elimina un elemento de un diccionario
diccionario.pop("nombre")

# obtiene un elemento  dict_items iterables
diccionario.items()

print(diccionario)

""" print(claves) """