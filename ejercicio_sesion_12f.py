#Escriba un algoritmo que pida un número al usuario y lo muestre 5 veces en pantalla.
numero = int(input("Ingrese un numero: "))
x = 1
while x <= 5:
    print("Iteración", x, " -> ", numero)
    x = x + 1