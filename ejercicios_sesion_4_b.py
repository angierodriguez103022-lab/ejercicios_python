# Una tienda vende tres productos. El programa pide el nombre y precio unitario de cada uno, junto con la cantidad comprada. Calcula el subtotal, el IVA del 19% y el total a pagar, y los muestra como una factura.

#objetivo
#calcular subtotal de los tres productos
#calcular el IVA de los tres productos
#calcular el total a pagar de los tres productos

producto_uno = input("Ingrese el nombre del primer producto: ")
valor_producto_uno = float(input("Ingrese el precio unitario del primer producto: "))
cantidad_producto_uno = int(input("Ingrese la cantidad comprada del primer producto: "))

print("-"*40)

producto_dos = input("Ingrese el nombre del segundo producto: ")
valor_producto_dos = float(input("Ingrese el precio unitario del segundo producto: "))
cantidad_producto_dos = int(input("Ingrese la cantidad comprada del segundo producto: "))

print("-"*40)

producto_tres = input("Ingrese el nombre del tercer producto: ")
valor_producto_tres = float(input("Ingrese el precio unitario del tercer producto: "))
cantidad_producto_tres = int(input("Ingrese la cantidad comprada del tercer producto: "))

print("-"*40)

valor_total_producto_uno = valor_producto_uno*cantidad_producto_uno
valor_total_producto_dos = valor_producto_dos*cantidad_producto_dos
valor_total_producto_tres = valor_producto_tres*cantidad_producto_tres

subtotal = valor_total_producto_uno + valor_total_producto_dos + valor_total_producto_tres
impuesto = subtotal * 0.19
total_por_pagar = subtotal + impuesto

print("Detalle factura de compra")
print("-"*40)
print("1. ", producto_uno, "| valor: ", valor_producto_uno, "| cantidad: ", cantidad_producto_uno, "| total: ", valor_total_producto_uno, "\n2. ", producto_dos, "| valor: ", valor_producto_dos, "| cantidad: ", cantidad_producto_dos, "| total: ", valor_total_producto_dos, "\n3. ", producto_tres, "| valor: ", valor_producto_tres, "| cantidad: ", cantidad_producto_tres, "| total: ", valor_total_producto_tres)
print(f"SUBTOTAL: {subtotal:.2f}")
print(f"IVA (19%): {impuesto:.2f}")
print(f"TOTAL POR PAGAR: {total_por_pagar:.2f}")