#Escriba un algoritmo que pida un número al usuario y muestre todos los números desde 1 hasta ese número.
numero = int(input("Ingrese un número: "))
contador = 1
while contador <= numero:
    print("Iteración No.",contador,":",contador)
    contador = contador + 1