# List crea una lista
lista = list(["Hola", "Mundo", 34])

# DEvulve la cantidad de elementos
resultado = len(lista)

#agrea un elemento
lista.append("JAJAJAJAJAJAJA")

# agrega un elemnto en un indice especifico
lista.insert(2, "Python")

# agregando mas de 1 elemento
lista.extend([False, 2030])

# Eliminando un elemento de una lista con el indice
lista.pop(0)

# Remuevev un elemnto por el valor del elemnto
lista.remove("Python")

# Elimina toda la lista
""" lista.clear() """

# No muestra las cadenas de texto
# si usamos reverse invierte el orden
""" lista.sort(reverse=True) """

# Invierte los elementos de una lista
lista.reverse()

print(lista)

