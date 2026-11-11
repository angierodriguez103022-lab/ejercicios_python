# Un supermercado realiza una promoción mediante la cual el cliente recibe un descuento dependiendo de un número entero entre 1 y 100 que se escoge al azar. Solicite el monto total de la compra (en USD) y el número que le tocó al cliente. Aplique las siguientes reglas:
# • Si el número es menor a 74: el descuento es del 15 % sobre el total de la compra.
# • Si el número es mayor o igual a 74: el descuento es del 20 % sobre el total de la compra.
# Salida esperada: valor del descuento aplicado y total a pagar.
import random
total_compra = float(input("Ingrese el total de la compra: "))
numero_ganador = random.randint(1, 100)
print("El número ganador es: ",numero_ganador)
if numero_ganador < 74:
    descuento = total_compra * 0.15
    total_con_descuento = total_compra - descuento
    print(f"Descuento aplicado del 15%: ${descuento:,.0f} \nTotal por pagar: ${total_con_descuento:,.0f}")
else:
    descuento = total_compra * 0.20
    total_con_descuento = total_compra - descuento
    print(f"Descuento aplicado del 20%: ${descuento:,.0f} \nTotal por pagar: ${total_con_descuento:,.0f}")