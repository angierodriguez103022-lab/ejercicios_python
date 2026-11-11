# Ejercicio 5. Cotización de un evento: matrimonio o cumpleaños Un organizador de eventos cotiza una fiesta. El programa pide el número de invitados, el costo por plato, el costo de la decoración y el costo de la música. Calcula el subtotal, un 15% adicional por administración y el valor total del evento, además del valor por invitado.
print("="*20, " COTIZACIÓN DE UN EVENTO ", "="*20)

numero_invitados = int(input("Ingrese el número de invitados al evento: "))
costo_plato = float(input("Ingrese el costo por plato: "))
costo_decoracion = float(input("Ingrese el costo total de la decoración: "))
costo_musica = float(input("Ingrese el costo total de la música: "))

platos = costo_plato * numero_invitados
subtotal = platos + costo_decoracion + costo_musica
adicional = subtotal * 0.15
total_evento = subtotal + adicional
costo_por_persona = total_evento / numero_invitados

print("="*20, "DETALLE COTIZACIÓN", "="*20)
print(f"El número de invitados corresponde a: {numero_invitados:,.0f} \nEl costo por plato corresponde a: $ {costo_plato:,.0f} pesos \nEl costo de la decoración corresponde a: $  {costo_decoracion:,.0f} pesos \nEl costo de la música corresponde a: $ {costo_musica:,.0f} pesos \nSubtotal: $ {subtotal:,.0f} pesos \nAdministración: $ {adicional:,.0f} pesos \nValor total del evento: $ {total_evento:,.0f} pesos \nEl valor por invitado corresponde a: $ {costo_por_persona:,.0f} pesos")