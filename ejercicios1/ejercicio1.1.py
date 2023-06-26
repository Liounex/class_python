# Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
d_curso = 1.5

# Duracion de crudo
c_promedio = 5
c_d = 3.5

# diferencias de duracion
dif = 100 - d_curso / otros_cursos_min * 100
dif2 = 100 - d_curso * 1000 // otros_cursos_max / 10
dif3 = 100 - d_curso / otros_cursos_promedio * 100

# tiempo vacio removido
dif_c = 100 - otros_cursos_promedio * 1000 // c_promedio / 10
dif_cd = 100 - d_curso * 1000 // c_d / 10

# Diferencia de duracio
print("-------------------")
print(f"el curso d_curso dura un {dif}% menos que el mas rapido")
print(f"el curso d_curso dura un {dif2}% menos que el mas rapido")
print(f"el curso d_curso dura un {dif3}% menos que el mas rapido")
print("-------------------")

# Cantidad de espacio vacio que se remueve
print("-------------------")
print(f"Un curso promedio elimina un  {dif_c}% de tiempo vacio")
print(f"Este curso elimina el {dif_cd}% de tiempo vacio")
print("-------------------")

# mostrando direrencoia si dfura 10 hras
print("-------------------")
print(f"Ver 10 hras de este curso equivale a ver {otros_cursos_promedio * 100 // d_curso / 10} horas de otros cursos")
print(f"Ver 10 hras de otros curso equivale a ver {d_curso * 100 // otros_cursos_promedio / 10} horas de este cursos")
print("-------------------")