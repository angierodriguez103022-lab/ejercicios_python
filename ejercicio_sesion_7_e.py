# Una persona enferma de 70 kg se encuentra en reposo y desea saber cuántas calorías consume su cuerpo durante el tiempo total que realice una actividad. Las únicas actividades permitidas son dormir o estar sentado en reposo. Solicite la actividad realizada (1 = dormir, 2 = sentado en reposo) y la cantidad de minutos que la realizó. Aplique los siguientes consumos:
# • Dormido: 1,08 calorías por minuto.
# • Sentado en reposo: 1,66 calorías por minuto.
# Salida esperada: total de calorías consumidas durante la actividad.
print("="*20, " PACIENTE ", "="*20)

ejercicio = int(input("Ingrese la actividad realizada (1 = dormir, 2 = sentado en reposo): "))
minutos_actividad = int(input("Ingrese la cantidad de minutos implementados en la actividad: "))

if ejercicio == 1:
    calorias = minutos_actividad * 1.08
else:
    calorias = minutos_actividad * 1.66

print(f"El total de calorias consumidas durante la actividad, corresponde a: {calorias:,.1f}")