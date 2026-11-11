# Enunciado: En un restaurante, una familia ordena varios platos. El mesero informa el subtotal antes de impuestos. En tu ciudad, el IVA se cobra como un porcentaje del subtotal. Además, la familia desea dejar una propina, también expresada como porcentaje del subtotal. Se te pide calcular el total a pagar.
print("="*20, " RESTAURANTE ", "="*20)
subtotal = float(input("Ingrese el subtotal de la orden: "))
porcentaje_impuesto = float(input("Ingrese el porcentaje de IVA a aplicar: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina a aplicar: "))

iva = subtotal * (porcentaje_impuesto / 100)
propina = subtotal * (porcentaje_propina / 100)
total_pagar = subtotal + iva + propina

print("="*20, "DETALLE CUENTA", "="*20)
print(f"Subtotal: ${subtotal:,.0f} \nIVA: ${iva:,.0f} \nPropina: ${propina:,.0f} \nEl total a pagar corresponde a: ${total_pagar:,.0f}")