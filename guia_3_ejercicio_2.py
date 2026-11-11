# Gamer Zone cobra una entrada por jugador, una tarifa por cada hora de juego y un refrigerio para cada visitante. El programa debe calcular el costo de la visita grupal y el valor que paga cada persona.
# Datos que debe solicitar el programa
# • Responsable de la reserva 
# • Precio por hora y jugador
# • Número de jugadores 
# • Precio del refrigerio por jugador
# • Precio de entrada por jugador 
# • Porcentaje de descuento grupal
# • Horas de juego por jugador
print("="*20, " GAMER ZONE ", "="*20)

responsable_reserva = input("Ingresar el nombre del responsable de la reserva: ")
precio_entrada = float(input("Ingrese el precio de entrada por jugador: "))
precio_hora = float(input("Ingrese el precio por hora: "))
horas_juego_jugador = float(input("Ingrese las horas de juego por jugador: "))
numero_jugadores = int(input("Ingrese el número de jugadores: "))
precio_refrigerio = float(input("Ingrese el precio del refrigerio por jugador: "))
porcentaje_descuento = float(input("Ingrese el procentaje de descuento grupal: "))

costo_entrada = precio_entrada * numero_jugadores
tarifa_hora_juego = precio_hora * horas_juego_jugador
costo_refrigerio = precio_refrigerio * numero_jugadores

total_visita = costo_entrada + tarifa_hora_juego + costo_refrigerio
descuento = total_visita * (porcentaje_descuento / 100)
total_con_descuento = total_visita - descuento

total_por_persona = total_con_descuento / numero_jugadores

print("="*20, "DETALLE RESERVA", "="*20)
print(f"Nombre cliente: {responsable_reserva} \nPrecio entrada: ${costo_entrada:,.0f} pesos \nHoras de juego: {horas_juego_jugador:,.0f} h \nNúmero de jugadores: {numero_jugadores:,.0f} \nSubtotal: $ {total_visita:,.0f} pesos \nDescuento: $ {descuento:,.0f} pesos \nTotal por pgar: ${total_con_descuento:,.0f} pesos \nCosto por persona: ${total_por_persona:,.0f} pesos")