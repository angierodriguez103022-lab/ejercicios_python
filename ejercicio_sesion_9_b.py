# Edad de una persona
#0 a 5 años  grupo de niños pequeños
#6 a 12 niños grandes 
#13 a 17 adolescentes
#18 a 65 adultos
#66 a 100 adulto mayor

edad = int(input("Ingrese la edad: "))
genero = input("Ingrese 'm' para mujer o 'h' para bomre: ").lower()

if genero != "m" and genero != "h":
    print("Ingrese nuevamente el genero")
else: 
    if edad  > 0 and edad <= 5:
        if genero == "m":
            print("Es una niña pequeña")
        else:
            print("Es un niño pequeño")
    elif edad >= 6 and edad <= 12:
        print("Es un niño grande")
    elif edad >= 13 and edad <= 17:
        print("Es un adolescente")
    elif edad >= 18 and edad <= 65:
        print("Es un adulto")
    elif edad >= 66 and edad <= 100:
        print("Es un adulto mayor")
    else:
        print("No ingresó una edad valida!!!")