#3. Mostrar números impares del 1 al 15 Escriba un algoritmo que muestre todos los números impares entre 1 y 15.

print("="*20, " NÚMERO IMARES DEL 1 AL 15 ", "="*20)

x = 1
while x < 15:
    x = x + 2
    if x % 2 == 1: 
        print(x)