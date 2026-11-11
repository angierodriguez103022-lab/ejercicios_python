#3. Mostrar números pares del 1 al 20 Escriba un algoritmo que muestre todos los números pares entre 1 y 20. // numero % 2 == 0 (es par)

print("="*20, " NÚMERO PARES DEL 1 AL 20 ", "="*20)

x = 1
while x <= 20:
    x = x + 1
    if x % 2 == 0: 
        print(x)

# x = 2
# while x <= 20:
#     print(x)
#     x = x + 2