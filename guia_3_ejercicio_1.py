# Café Pixel vende sándwiches y jugos por internet. Su propietaria necesita calcular el costo de un pedido, aplicar un descuento a los productos y agregar el valor del domicilio.
# Datos que debe solicitar el programa
# • Nombre del cliente YA
# • Precio unitario del jugo YA
# • Cantidad de sándwiches YA
# • Porcentaje de descuento YA
# • Precio unitario del sándwich YA 
# • Costo fijo del domicilio YA
# • Cantidad de jugos YA
print("="*20, " CAFÉ PIXEL ", "="*20)

nombre_cliente = input("Ingrese el nombre del cliente: ")
precio_unitario_jugo = float(input("Ingrese el precio unitario del jugo: "))
cantidad_jugo = int(input("Ingrese la cantidad de jugos: "))
precio_unitario_sandwich = float(input("Ingrese el precio unitario del Sándwich: "))
cantidad_sandwich = int(input("Ingrese la cantidad de Sándwiches: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
domicilio = float(input("Ingrese el costo del domicilio: "))

total_jugo = precio_unitario_jugo * cantidad_jugo
total_sandwich = precio_unitario_sandwich * cantidad_sandwich
costo_pedido = total_jugo + total_sandwich
descuento = costo_pedido * (porcentaje_descuento / 100)
total_pedido = costo_pedido - descuento + domicilio

print("="*20, "DETALLE PEDIDO", "="*20)
print(f"Nombre cliente: {nombre_cliente} \nJugo: precio unitario: ${precio_unitario_jugo:,.0f} pesos | cantidad: {cantidad_jugo:,.0f} | Total: ${total_jugo:,.0f} pesos \nSandwich: precio unitario: ${precio_unitario_sandwich:,.0f} pesos | cantidad: {cantidad_sandwich} | Total: ${total_sandwich:,.0f} pesos \nSubtotal: ${costo_pedido:,.0f} pesos \nDescuento aplicado: $ {descuento:,.0f} pesos \nTotal por pagar: ${total_pedido:,.0f} pesos")