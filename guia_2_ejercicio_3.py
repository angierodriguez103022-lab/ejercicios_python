# Ejercicio 3. Cuánto cuesta realmente un streaming al año Una persona tiene tres suscripciones (por ejemplo, música, video y almacenamiento). El programa pide el precio mensual de cada una y calcula el gasto mensual total, el gasto anual y cuánto representa cada una del total, en porcentaje.
print("="*20, " COSTO REAL STREAMING AL AÑO ", "="*20)

precio_mensual_spotify = float(input("Ingrese el costo mensual de la membresía de Spotify: "))
precio_mensual_icloud = float(input("Ingrese el costo mensual de la membresía de iCloud: "))
precio_mensual_netflix = float(input("Ingrese el costo mensual de la membresía de Netflix: "))

gasto_mensual_total = precio_mensual_spotify + precio_mensual_icloud + precio_mensual_netflix
gasto_anual_total = gasto_mensual_total * 12
porcentaje_spotify = (precio_mensual_spotify / gasto_mensual_total) * 100
porcentaje_icloud = (precio_mensual_icloud / gasto_mensual_total) * 100
porcentaje_netflix = (precio_mensual_netflix / gasto_mensual_total) * 100

print("="*20, "DETALLE STREAMING ANUAL", "="*20)
print(f"El costo mensual de la membresía de Spotify corresponde a: $ {precio_mensual_spotify:,.0f} pesos \nEl costo mensual de la membresía de iCloud corresponde a: $ {precio_mensual_icloud:,.0f} pesos \nEl costo mensual de la membresía de Netflix corresponde a: $ {precio_mensual_netflix:,.0f} pesos \nGasto mensual: $ {gasto_mensual_total:,.0f} pesos \nGasto anual: $ {gasto_anual_total:,.0f} pesos \nMensualmente, porcentualmente representa:\nSpotify: {porcentaje_spotify:,.1f}% \niCloud: {porcentaje_icloud:,.1f}% \nNetflix: {porcentaje_netflix:,.1f}%")