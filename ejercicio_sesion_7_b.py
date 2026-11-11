# Ejercicio 4. Venta al por mayor con descuento y obsequio
# Un supermercado vende cierto producto por docenas a un precio unitario por docena de 20 USD. Por una promoción se aplican las siguientes reglas según la cantidad de docenas que compre el cliente:
# • Si compra más de 3 docenas: se aplica un descuento del 15 % sobre el monto bruto y, además, se obsequia una unidad del producto por cada docena comprada.
# • Si compra 3 docenas o menos: se aplica un descuento del 10 % sobre el monto bruto y no hay obsequio.
# Salidas esperadas: monto bruto de la compra, valor del descuento, monto neto a pagar y cantidad de unidades de obsequio.
print("="*20, " VENTA AL POR MAYOR CON DESCUENTO Y OBSEQUIO ", "="*20)

docenas_compradas = int(input("Ingrese la cantidad de docenas compradas"))
valor_docena = 20
total_bruto = docenas_compradas * valor_docena

if docenas_compradas > 3:
    descuento = total_bruto * 0.15
    obsequio = docenas_compradas
    print(f"Monto bruto: ${total_bruto:,.0f} \nDescuento: ${descuento:,.0f}")