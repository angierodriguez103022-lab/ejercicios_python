#Match
print("¿Qué quieres hacer?: 1.Suma 2.Resta 3.Multiplicación 4.División")
opcion = int(input("Ingrese la opción: "))

if opcion == 1:
    numero_uno = int(input("Ingrese el primer número: "))
    numero_dos = int(input("Ingrese el segundo número: "))
    total = numero_uno + numero_dos
    print(f"El total de la suma es: {total:,.0f}")
elif opcion == 2:
    numero_uno = int(input("Ingrese el primer número: "))
    numero_dos = int(input("Ingrese el segundo número: "))
    total = numero_uno - numero_dos
    print(f"El total de la resta es: {total:,.0f}")
elif opcion == 3:
    numero_uno = int(input("Ingrese el primer número: "))
    numero_dos = int(input("Ingrese el segundo número: "))
    total = numero_uno * numero_dos
    print(f"El total de la multiplicación es: {total:,.0f}")
elif opcion == 4:
    numero_uno = int(input("Ingrese el primer número: "))
    numero_dos = int(input("Ingrese el segundo número: "))
    if numero_dos != 0:
        total = numero_uno / numero_dos
        print(f"El total de la división es: {total:,.0f}")
    else:
        print("No es posible dividir en 0 ❌")
else:
    print("Opción incorrecta ❌")