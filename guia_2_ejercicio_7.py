# Ejercicio 7. Plan de ahorro para comprar una moto Una persona quiere comprar una moto. El programa pide el precio de la moto, la cuota inicial que ya tiene ahorrada y el ahorro mensual que puede hacer. Calcula cuánto le falta y en cuántos meses y años lo logrará (usando división entera y residuo para mostrar años y meses completos).
print("="*20, " PLAN DE AHORRO COMPRA DE MOTO ", "="*20)

precio_moto = float(input("Ingrese el precio de la moto: $"))
cuota_inicial = float(input("Ingrese el monto de la cuota inicial: $"))
ahorro_mensual = float(input("Ingrese el ahorro mensual: $"))

faltante_moto = precio_moto - cuota_inicial
meses_por_pagar = (faltante_moto + ahorro_mensual - 1) // ahorro_mensual
sobra = faltante_moto % ahorro_mensual

anio = 12
anios = meses_por_pagar // anio
meses = meses_por_pagar % anio

print("="*20, "DETALLE PLAN DE AHORRO", "="*20)
print(f"El precio total de la moto corresponde a: ${precio_moto:,.1f} \nLa cuota inicial corresponde a: ${cuota_inicial:,.0f} \nEl ahorro mensual corresponde a: ${ahorro_mensual:,.0f} \nTotal por pgar: ${faltante_moto:,.0f} \nEl tiempo para pagar es de: {anios:,.0f} año(s) | {meses:,.0f} mes(es)")