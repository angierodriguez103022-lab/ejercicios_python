#pedir un número al usuraio y generar un número aleatorio, este será el número secreto
#si  este número es igual al que digito el usuario, saldra un mensaje, Ganaste de lo contrario el mensaje sera, "Perdiste". El usuario tendra 3 intentos de adivinar el número
import random
print("="*20, "¡Tienes 3 intentos para adivinar el número secreto entre 1 y 10!","="*20)
numero_secreto = random.randint(1,10)
contador = 1

while contador <= 3:
    numero = int(input(f"Intento {contador}/3 - Ingrese un número: "))
    if numero > 10:
        print("Número fuera del rango")
        contador = 4
    else:
        if numero == numero_secreto:
            print("Ganaste ✅")
            contador = 4
        else:
            print("Perdiste ❌")
        contador = contador + 1

if numero != numero_secreto:
    print(f"Te quedaste sin intentos 😥. El número secreto era: {numero_secreto}")