# Ejercicio 2. Propina y división de la cuenta en un restaurante Un grupo de amigos termina de comer. El programa pide el valor de la cuenta, el porcentaje de propina y el número de personas. Calcula la propina, el total con propina y cuánto debe pagar cada uno.
print("="*20, " PROPINA Y DIVISIÓN DE LA CUENTA EN UN RESTAURANTE ", "="*20)

valor_cuenta = float(input("Ingrese el valor de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de la propina: "))
numero_personas = int(input("Ingrese el número de personas para dividir la cuenta: "))

total_propina = valor_cuenta * (porcentaje_propina / 100)
total_cuenta = valor_cuenta + total_propina
pagar_cada_uno = total_cuenta / numero_personas

print("="*20, "DETALLE CUENTA RESTAURANTE", "="*20)
print(f"El valor de la cuenta corresponde a: $ {valor_cuenta:,.0f} pesos \nEl porcentaje de la propina corresponde a: {porcentaje_propina:,.0f}% \nNúmero de personas para dividir la cuenta: $ {numero_personas:,.0f} \nPropina: $ {total_propina:,.0f} pesos \nTotal por pagar: {total_cuenta:,.0f} pesos \nCada persona debe pagar: $ {pagar_cada_uno:,.0f} pesos")