# Edad de una persona
#0 a 5 años  grupo de niños pequeños
#6 a 12 niños grandes 
#13 a 17 adolescentes
#18 a 65 adultos
#66 a 100 adulto mayor

edad = int(input("Ingrese la edad: "))

if edad  > 0 and edad <= 5:
    print("Es un niño pequeño")

if edad >= 6 and edad <= 12:
        print("Es un niño grande")
    
if edad >= 13 and edad <= 17:
    print("Es un adolescente")

if edad >= 18 and edad <= 65:
    print("Es un adulto")

if edad >= 66 and edad <= 100:
    print("Es un adulto mayor")

if edad > 100:
    print("No ingresó una edad valida!!!")

print("Fin")