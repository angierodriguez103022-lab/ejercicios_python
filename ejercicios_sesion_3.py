# 4. Facturación Básica de Punto de Venta: Un comercio requiere calcular la factura de un cliente. Solicita el precio unitario de un producto y la cantidad comprada. Calcula el subtotal, aplica el IVA (19%) y muestra el subtotal, el impuesto y el total a pagar.

print("Facturación Básica de Punto de Venta")

precio_producto = float(input("Ingrese el precio unitario del producto: "))
cantidad_producto = int(input("Ingrese la cantidad del producto: "))
subtotal = precio_producto * cantidad_producto
impuesto = subtotal * 0.19
total_pagar = subtotal + impuesto
print("-"*40)
print("Detalle de factura. \nSubtotal:", subtotal, "\nIVA:", impuesto, "\nTotal por pagar:", total_pagar)