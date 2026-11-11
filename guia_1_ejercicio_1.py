# 1. Calculadora de Saludo Personalizado: Escribe un programa que solicite al usuario su nombre y su edad. Posteriormente, debe imprimir un mensaje de bienvenida informando cuántos años cumplirá el usuario el próximo año. 

print("Calculadora de saludo personalizado")

nombre = input("\nPor favor digite su nombre: ")
edad = int(input("Por favor digite su edad: "))
edad_proxima = edad + 1

print("Bienvenid@",nombre, "el próximo año cumpliras",edad_proxima, "años.")