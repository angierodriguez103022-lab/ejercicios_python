# 7. Calculadora de Depreciación en Línea Recta: Para efectos contables, solicita el valor de adquisición de un activo, su valor de salvamento y la vida útil en años. Muestra la depreciación anual y el valor contable restante tras el primer año: Depreciación = (Valor Adquisición - Valor Salvamento) / Vida Útil. 
print("="*20, "CALCULADORA DE DEPRECIACIÓN EN LÍNEA RECTA", "="*20)

valor_adquisicion = float(input("Ingrese el valor de adquisición del activo: "))
valor_salvamento = float(input("Ingrese el avlor de salvamento del activo: "))
vida_util = int(input("Ingrese la vida útil en año del activo: "))

depreciacion = (valor_adquisicion - valor_salvamento) / vida_util

valor_contable_estante = valor_adquisicion - depreciacion

print("="*20, "DETALLE DEPRECIACIÓN", "="*20)
print(f"El valor de adquisición del activo corresponde a: $ {valor_adquisicion:,.0f} \nEl valor de salvamento del activo corresponde a: $ {valor_salvamento:,.0f} \nLa vida útil del activo corresponde a: {vida_util:,.0f} \nDepreciación anual: $ {depreciacion:,.0f} \nEl valor contable restante tras el primer año corresponde a: $ {valor_contable_estante:,.0f}")