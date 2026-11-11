# Escribe un programa que decida si se aprueba un crédito. Primero pide la edad (entero). Si es menor de 18, debe mostrar No cumples la edad mínima. Si tiene 18 años o más, debe preguntar si tiene empleo (si o no). Si no tiene empleo, debe mostrar Necesitas un empleo para solicitar el crédito. Si tiene empleo, debe pedir los ingresos mensuales en pesos (entero): con 2000000 o más debe mostrar Crédito aprobado; con menos, debe mostrar Ingresos insuficientes.
print("="*20, " APROBACIÓN CRÉDITO ", "="*20)

edad = int(input("Ingrese la edad del solicitante: "))

if edad >= 18:
    empleo = input("¿Tiene empleo (si / no): ").lower()
    if empleo == "si":
        ingreso_mensual = int(input("Ingrese los ingresos mensuales: $"))
        if ingreso_mensual >= 2000000:
            print("Crédito aprobado ✅")
        else:
            print("Ingresos insuficientes ❌")
    else:
        print("Necesita empleo para solicitar el crédito ❌")
else:
    print("No cumple la edad mínima ❌")