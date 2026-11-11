# 2. Conversor de Temperatura: Diseña un algoritmo que lea una temperatura en grados Celsius (°C) y la convierta a Fahrenheit (°F) y Kelvin (K) usando las fórmulas: °F = (°C * 9/5) + 32  y  K = °C + 273.15.
print("Conversor de Temperatura\n")

grados_celsius = float(input("Ingrese la tempreatura a convertir: "))

fahrenheit =  (grados_celsius * 9/5) + 32
kelvin =  grados_celsius + 273.15

print("-"*20)
print(f"Temperatura en grados Celsius: {grados_celsius:.2f} °C\nTemperatura en grados Fahrenheit: {fahrenheit:.2f} °F\nTemperatura en grados Kelvin: {kelvin:.2f} K")