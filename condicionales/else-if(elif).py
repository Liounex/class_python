# Sigue en if - else

ingreso_mensual = 81000
gasto_mensual = 80000

# If anidados y elif
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien con en el mundo")
    else:
        print("Estas ganstando de mas")
elif ingreso_mensual > 1000:
    print("Estas bien en Perú")
elif ingreso_mensual > 500:
    print("Estas bien en Argentina")
elif ingreso_mensual > 200:
    print("Estas bien en Venezuela")
else:
    print("Eres Pobre")
