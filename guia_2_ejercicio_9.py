# Ejercicio 9. Rentabilidad de una inversión en un CDT Un ahorrador abre un CDT. El programa pide el capital invertido, la tasa efectiva anual y el plazo en años. Calcula el valor final con interés compuesto (capital x (1 + tasa)años), la ganancia total y la ganancia promedio por mes.
print("="*20, " RENTABILIDAD INVERSIÓN EN CDT ", "="*20)

capital = float(input("Ingrese el monto de capital invertido: $"))
tasa_anual = float(input("Ingrese la tasa efectiva anual: "))
plazo = float(input("Ingrese el pazo en años: "))

tasa = tasa_anual / 100
valor_final = capital * (1 + tasa) ** plazo

meses_anio = 12
meses_totales = plazo * meses_anio
ganancia_total = valor_final - capital
ganancia_prom_mes = ganancia_total / meses_totales

print("="*20, "DETALLE INVERSIÓN", "="*20)
print(f"El monto de capital invertido corresponde a ${capital:,.0f} \nLa tasa efectiva anual correpsonde a: ${tasa_anual:,.0f} \nEl plazo en años corresponde a: {plazo:,.0f} \nValor final con interés compuesto: ${valor_final:,.0f} \nGanancia total: ${ganancia_total:,.0f} \nGanancia promedio por mes: ${ganancia_prom_mes:,.2f}")