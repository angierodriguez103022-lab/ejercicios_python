#Escriba un algoritmo que muestre la tabla de multiplicar del 3 del 1 al 10.

multiplicador = int(input("Ingrese el multiplicador: "))
contador = 1
while contador <= 10:
    resultado = multiplicador * contador
    print(multiplicador,"x",contador,"=",resultado)
    #print(f"3 x {contador} = {multiplicador*contador}")
    contador = contador + 1