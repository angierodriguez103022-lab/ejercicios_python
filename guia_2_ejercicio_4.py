# Ejercicio 4. Huella de carbono de un desplazamiento Una empresa quiere medir el impacto de los viajes de sus empleados. El programa pide los kilómetros diarios recorridos, los días laborados al mes y el factor de emisión del vehículo (kg de CO2 por km). Calcula las emisiones mensuales y anuales, y cuántos árboles se necesitarían para compensarlas si cada árbol absorbe 22 kg de CO2 al año.
print("="*20, " HUELLA DE CARBONO DE UN DESPLAZAMIENTO ", "="*20)

km_recorridos = float(input("Ingrese los kilómetros diarios recorridos: "))
dias_laborados = int(input("Ingrese el número de días laborados al mes: "))
factor_emision = float(input("Ingrese el factor de emisión del vehículo (kg de CO₂ por km) entre 1.0 y 1.3: "))

km_mes = km_recorridos * dias_laborados
emision_mensual = km_mes * factor_emision
emision_anual = emision_mensual * 12
arboles = emision_anual / 22

print("="*20, "DETALLE HUELLA DE CARBONO ANUAL", "="*20)
print(f"Los kilómetros diarios recorridos corresponde a: {km_recorridos:,.0f}Km \nLos días laborados al mes corresponde a: {dias_laborados:,.0f} días \nEl factor de emisión corresponde a: {factor_emision:,.0f} Kg de CO₂ por Km \nEmisión mensual: {emision_mensual:,.0f} Kg de CO₂ al mes \nEmisión anual: {emision_anual:,.0f} Kg de CO₂ al año \nSe necesitan {round(arboles,0)} árboles de compensación")