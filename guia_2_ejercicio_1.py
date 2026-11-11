# Ejercicio 1. Ganancia de un emprendedor en Mercado Libre Una persona vende un producto en línea. El programa pide el precio de venta, el costo de compra, el porcentaje de comisión de la plataforma y el costo del envío que asume el vendedor. Calcula la comisión en pesos, el costo total y la ganancia neta por unidad. Luego pide cuántas unidades vendió en el mes y muestra la ganancia mensual.
print("="*20, " GANANCIA DE UN EMPRENDEDOR EN MERCADO LIBRE ", "="*20)

precio_venta = float(input("Ingrese el precio de venta: "))
costo_compra = float(input("Ingrese el costo de compra: "))
porcentaje_comision = float(input("Ingrese el porcentaje de comisión de la plataforma: "))
costo_envio = float(input("Ingrese el costo del envío: "))

comision = precio_venta * (porcentaje_comision / 100)
costo_total_unidad = costo_compra + comision + costo_envio
ganancia_neta = precio_venta - costo_total_unidad

unidades_mes = int(input("Ingrese las unidades vendidas en el mes: "))
ganancia_mensual = ganancia_neta * unidades_mes

print("="*20, "DETALLE GANANCIA EMPRENDEDOR", "="*20)
print(f"El precio de venta corresponde a: $ {precio_venta:,.0f} pesos \nEl costo de compra corresponde a: $ {costo_compra:,.0f} pesos \nEl porcentaje de comisión corresponde al: {porcentaje_comision:,.0f}% \nEl costo del envío corresponde al: $ {costo_envio:,.0f} pesos  \nComisión: $ {comision:,.0f} pesos \nCosto total: $ {costo_total_unidad:,.0f} pesos \nGanancia neta por unidad: $ {ganancia_neta:,.0f} pesos \nLa ganancia mensual corresponde a: $ {ganancia_mensual:,.0f} pesos")