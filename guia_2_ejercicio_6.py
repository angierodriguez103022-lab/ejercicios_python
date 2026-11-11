# Ejercicio 6. Tiempo de descarga de un archivo Un estudiante necesita descargar un curso en video. El programa pide el tamaño del archivo en GB y la velocidad de su internet en Mbps. Convierte las unidades (1 GB = 8000 megabits aproximadamente) y calcula cuánto demora la descarga, expresado en horas, minutos y segundos.
print("="*20, " TIEMPO DE DESCARGA DE UN ARCHIVO ", "="*20)

tamano_archivo = float(input("Ingrese el tamaño del archivo en GB: "))
velocidad_internet = float(input("Ingrese la velocidad de su internet en Mbps: "))

tiempo_hora = 3600 #segundos
tiempo_minutos = 60 #segundos
megabit_gb = 8000
conversion = tamano_archivo * megabit_gb

tiempo_descarga = conversion / velocidad_internet
tiempo_entero = int(tiempo_descarga)

horas = tiempo_entero // tiempo_hora
residuo = tiempo_entero % tiempo_hora
minutos = residuo // tiempo_minutos
residuo = residuo % tiempo_minutos
segundos = residuo

print("="*20, "DETALLE DESCARGA", "="*20)
print(f"El tamaño del archivo corresponde a: {tamano_archivo:,.1f} GB \nLa velocidad del Internet corresponde a: {velocidad_internet:,.0f} Mbps \nEl tiempo de descarga es de:  {horas:,.0f} hora(s) | {minutos:,.0f} minuto(s) | {segundos:,.0f} segunddo(s)")