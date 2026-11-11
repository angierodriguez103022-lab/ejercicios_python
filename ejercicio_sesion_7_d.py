# Ejercicio 3. Cobro de estacionamiento
# En un estacionamiento se cobra 2 USD por cada hora o fracción de hora. Solicite el tiempo de permanencia del vehículo en horas y minutos enteros (por ejemplo: 2 horas y 15 minutos). Calcule e imprima el valor total que debe pagar el cliente.
# Aclaración: cualquier fracción de hora (es decir, cualquier cantidad de minutos mayor a 0) se cobra como una hora completa adicional. Ejemplo: 2 horas y 15 minutos se cobran como 3 horas → 6 USD.
print("="*20, " COBRO DE ESTABLECIMIENTO ", "="*20)

hora = int(input("Ingrese en horas la permanencía del vehículo: "))
minuto = int(input("Ingrese en minutos la permanencía del vehículo: "))

total_tiempo = hora

if minuto > 0:
    total_tiempo_min = total_tiempo + 1
    total_pagar = total_tiempo_min * 2
else:
    total_pagar = total_tiempo * 2

print(f"El tiempo de permanencia del vehículo corresponde a: {hora:,.0f} horas y {minuto:,.0f} minutos \nEl valor total a pagar por el cliente es: ${total_pagar:,.0f} USD")