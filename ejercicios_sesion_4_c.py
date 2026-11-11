# Un grupo de amigos termina de comer. El programa pide el valor de la cuenta, el porcentaje de propina y el número de personas. Calcula la propina, el total con propina y cuánto debe pagar cada uno.

valor_cuenta = float(input("Ingrese el valor de la cuenta: "))
porcentaje_propina = float(input("Ingrese la propina, solo de 1 a 100: "))
numero_persona = int(input("Ingrese el número de personas: "))

total_propina = valor_cuenta * (porcentaje_propina/100)
total_por_pagar = valor_cuenta + total_propina
paga_cada_uno = total_por_pagar / numero_persona

print("="*10, "DETALLE FACTURA", "="*10)
print(f"Valor inicial de la cuenta: $ {valor_cuenta:,.0f}")
print(f"Valor de la propina: $ {total_propina:,.0f}")
print(f"Total por pagar: $ {total_por_pagar:,.0f}")
print(f"Cada persona debe pagar: $ {paga_cada_uno:,.2f}")