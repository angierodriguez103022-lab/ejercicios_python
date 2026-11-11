# Una tienda vende un producto que cuesta 10 dolaraes. Primero el programa debe preguntar si el producto está disponible (si  o  no ). Si no está disponible, debe mostrar  Producto agotado  y no pedir nada más. Si está disponible, debe pedir el saldo dela persona (número entero): si el saldo es 10 dolares o más, debe mostrar Compra exitosa ; sies menor, debe mostrar  Saldo insuficiente.

stock = input("¿El producto está disponible? (Si / No): ")

if stock == "Si":
    saldo = int(input("Ingrese el saldo de la persona: $"))
    if saldo >= 10:
        print("Compra exitosa!!!")
    else:
        print("Saldo insuficiente!!!")
#else:
#    print("Producto agotado")
elif stock == "No":
    print("Producto agotado")
else:
    print("Disponibilidad incorrecta")