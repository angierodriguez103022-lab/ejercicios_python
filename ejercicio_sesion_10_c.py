# Escribe un programa que pida la edad (entero). Si la persona es menor de 18 años, debe mostrar Eres menor de edad y no pedir nada más. Si tiene 18 años o más, debe pedir el dinero que tiene (entero) para pagar una compra de 20000 pesos: si tiene 20000 o más, debe mostrar Compra realizada; si tiene menos, debe mostrar Dinero insuficiente.
print("="*20, " VERIFICACIÓN COMPRA ", "="*20)

edad = int(input("Ingrese la edad: "))

if edad >= 18:
    dinero = int(input("Ingrese el dinero que dispone para pagar la compra: $"))
    if dinero >= 20000:
        print("Compra realizada ✅")
    else:
        print("Dinero insuficiente ❌")
else:
    print("Eres menor de edad")