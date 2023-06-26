frase = input("Calcula el tiempo: ")

palabras_separadas = frase.split(" ")

cantidad_de_palabras = len(palabras_separadas)

if cantidad_de_palabras > 120:
    print("Mucho Texto")
    
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras} segundos en decirlos")
print(f"tardaste {cantidad_de_palabras * 100 // 2 *1.3 / 100} segundos en decirlos")