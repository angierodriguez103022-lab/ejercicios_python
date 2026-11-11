# 10. Proyección de Rendimiento con Interés Compuesto: Un fondo de inversión ofrece una tasa de interés nominal anual fija con capitalización mensual. Solicita el monto inicial (P), la tasa de interés anual (%) y la duración en meses (m). Calcula el monto acumulado (A) y la ganancia neta generada usando: A = P * (1 + (r / 100) / 12) ^ m.
print("="*20, "PROYECCIÓN DE RENDIMIENTO CON INTERESÉS COMPUESTO", "="*20)

monto_inicial = float(input("Ingrese el monto inicial: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual: "))
duracion_meses = int(input("Ingrese la duración en meses: "))

monto_acumulado = monto_inicial * (1 + (tasa_interes_anual / 100) / 12) ** duracion_meses
ganancia_neta = monto_acumulado - monto_inicial

print("="*20, "DETALLE RENDIMIENTO CON INTERÉS COMPUESTO", "="*20)
print(f"El monto inicial corresponde a: $ {monto_inicial:,.0f} pesos \n La tasa de interés anual corresponde a: {tasa_interes_anual:,.0f} % \nLa duración corresponde a: {duracion_meses:,.0f} meses \nMonto acumulado: $ {monto_acumulado:,.0f} pesos \nGanancia netada generada: $ {ganancia_neta:,.0f} pesos")