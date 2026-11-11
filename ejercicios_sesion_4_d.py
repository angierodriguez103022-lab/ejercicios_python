# Una persona tiene tres suscripciones (por ejemplo, música, video y almacenamiento). El programa pide el precio mensual de cada una y calcula el gasto mensual total, el gasto anual y cuánto representa cada una del total, en porcentaje.

pago_spotify = float(input("Ingrese el precio mensual de la suscripción a Spotify: "))
pago_icloud = float(input("Ingrese el precio mensual de la suscripción a iCloud: "))
pago_netflix = float(input("Ingrese el precio mensual de la suscripción a Netflix: "))

gasto_mensual = pago_spotify + pago_icloud + pago_netflix
gasto_anual = gasto_mensual * 12

porcentaje_spotify = (pago_spotify / gasto_mensual)*100
porcentaje_icloud = (pago_icloud / gasto_mensual)*100
porcentaje_netflix = (pago_netflix / gasto_mensual)*100

print("-"*40)
print(f"El gasto total mensual de las suscripciones corresponde a: $ {gasto_mensual:.0f}")
print(f"El gasto total anual de las suscripciones corresponde a: $ {gasto_anual:.0f}")
print("Mensualmente porcentualmente representa: ")
print(f"Spotify: {porcentaje_spotify:.2f}%\niCloud: {porcentaje_icloud:.2f}%\nNetflix: {porcentaje_netflix:.2f}%")