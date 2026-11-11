# Una lavandería de autoservicio tiene las siguientes tarifas fijas: lavar ropa cuesta $5 dolares por cada kilogramo de ropa y el ciclo de secado cuesta 3 dolares planos sin importar el peso. Un cliente lleva cierta cantidad de kilogramos de ropa, paga el lavado y el secado, y entrega un billete de determinada denominación. La máquina de cambio del negocio entrega el vuelto en monedas de $10, $5, $2 y 1 dolar dolares, priorizando siempre las monedas de mayor denominación. Diseña un algoritmo que lea el peso de la ropa en kilogramos y el valor del billete entregado, calcule el costo total del servicio, calcule el cambio total, determine cuántas monedas de cada denominación se deben entregar y muestre todos los resultados.
print("="*20, " LAVANDERÍA DE AUTOSERVICIO ", "="*20)
lavar_ropa = float(5) # por un kilogramo
secado = float(3)
denominacion_a = float(10)
denominacion_b = float(5)
denominacion_c = float(2)
denominacion_d = float(1)

ropa_kg = float(input("Ingrese el peso de la ropa en kilogramos a lavar: "))
billete_entregado = float(input("Ingrese la denominación del billete: $"))

costo_lavado = ropa_kg * lavar_ropa
costo_total_servicio = costo_lavado + secado
cambio_total = billete_entregado - costo_total_servicio

moneda_10 = cambio_total // denominacion_a
cambio_faltante = cambio_total % denominacion_a
moneda_5 = cambio_faltante // denominacion_b
cambio_faltante = cambio_faltante % denominacion_b
moneda_2 = cambio_faltante // denominacion_c
cambio_faltante = cambio_faltante % denominacion_c
moneda_1 = cambio_faltante

print("="*20, "DETALLE CUENTA", "="*20)
print(f"TARIFAS \nLavado ropa: ${lavar_ropa:,.0f} por cada kilogramo \nSecado: ${secado:,.0f}")
print("="*40)
print(f"El peso de la ropa a lavar corresponde a: {ropa_kg:,.1f}Kg \nCosto total: ${costo_total_servicio:,.0f} \nCambio total: ${cambio_total:,.0f} \nSu cambio se dará de la siguiente forma: Moneda $10: {moneda_10:,.0f} | Moneda $5: {moneda_5:,.0f} | Moneda $2: {moneda_2:,.0f} | Moneda $1: {moneda_1:,.0f}")