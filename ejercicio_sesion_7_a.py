#El precio de dos productos si el total de la compra es mayo a 100 dolares, se hara un descuento de 10% de los contrario no tiene descuento. Mostrar el toal sin descuento el descuento y el total despues de descuento
precio_producto_uno = float(input("Ingrese el valor del primer producto: $"))
precio_producto_dos = float(input("Ingrese el valor del segundo producto: $"))

total_compra = precio_producto_uno + precio_producto_dos
if total_compra > 100:
    descuento = total_compra * 0.10
    total_con_descuento = total_compra - descuento
    print(f"Total compra: ${total_compra:,.0f} \nDescuento: ${descuento:,.0f} \nTotal por pagar: ${total_con_descuento:,.0f}")
else:
    print(f"Total por pagar: {total_compra:,.0f} \nNo aplica descuento")