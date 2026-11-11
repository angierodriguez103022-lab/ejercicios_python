# Una persona vende un producto en línea. El programa pide el precio de venta, el costo de compra, el porcentaje de comisión de la plataforma y el costo del envío que asume el vendedor. Calcula la comisión en pesos, el costo total y la ganancia neta por unidad. Luego pide cuántas unidades vendió en el mes y muestra la ganancia mensual.

# Objetivo
# Calcular comisión en pesos
# Costo total
# Ganancia neta por unidad
# Ganancia mensual

# Datos a pedir
# El precio de venta
# El costo de compra
# El porcentaje de comisión de la plataforma
# El costo del envío

precio_venta = float(input("Ingrese el precio del venta del producto: "))
costo_compra = float(input("Ingrese el costo de la compra: "))
porcentaje_comision = float(input("Ingrese el porcentaje de comisión de la plataforma, solo de 1 a 100: "))
costo_envio = float(input("Ingrese el costo del envío: "))

conversion_porcentaje_com = porcentaje_comision / 100

total_comision = precio_venta * conversion_porcentaje_com
costo_total = costo_compra + total_comision + costo_envio
ganancia_unidad = precio_venta - costo_total

unidades_mes = int(input("Ingrese el número de unidades vendidas en el mes: "))
ganancia_mesual = unidades_mes * ganancia_unidad

print("-"*40)
print(f"Precio venta producto: ${precio_venta:,.1f}")
print(f"Precio compra producto: ${costo_compra:,.1f}")
print(f"Comisión plataforma: ${total_comision}")
print(f"Ganancia neta por unidad: ${ganancia_unidad:,.1f}")
print(f"Su ganancia mensual es de: ${ganancia_mesual:,.1f}")