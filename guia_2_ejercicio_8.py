# Ejercicio 8. Gasto de datos en un plan de celular Una persona tiene un plan con una cantidad de GB al mes. El programa pide los GB del plan, los minutos diarios que ve videos, los minutos diarios que usa redes sociales y el consumo en MB por minuto de cada actividad. Calcula el consumo diario y mensual (30 días) en GB y muestra la diferencia entre los GB del plan y el consumo mensual.
print("="*20, " GASTO DE DATOS EN PLAN DE CELULAR ", "="*20)

gb_plan = float(input("Ingrese los GB del plan: "))
min_diario_video = int(input("Ingrese los minutos diarios que ve videos: "))
consumo_mb_minuto_video = int(input("Ingrese el consumo en MB por minuto de ver videos: "))
min_redes_sociales = int(input("Ingrese los minutos diarios que usa en redes sociales: "))
consumo_mb_minuto_redes_sociles = int(input("Ingrese el consumo en MB por minuto para ver redes sociales: "))

consumo_diario_video = consumo_mb_minuto_video * min_diario_video
consumo_diario_redes = consumo_mb_minuto_redes_sociles * min_redes_sociales
consumo_diario = consumo_diario_video + consumo_diario_redes

gb = 1024
dias_mes = 30
consumo_diario_gb = consumo_diario / gb
consumo_mensual_gb = consumo_diario_gb * dias_mes
diferencia = gb_plan - consumo_mensual_gb

print("="*20, "DETALLE PLAN DE CELULAR", "="*20)
print(f"Los GB del plan corresponde a: {gb_plan:,.2f} \nMinutos diarios viendo videos {min_diario_video} \nConsumo en MB por minuto para ver videos: {consumo_mb_minuto_video:,.0f} \nMinutos diarios para redes sociales: {min_redes_sociales} \nConsumo en MB por minuto para redes sociales: {consumo_mb_minuto_redes_sociles:,.0f} \nConsumo diario: {consumo_diario_gb:,.2f} GB \nConsumo mensual: {consumo_mensual_gb:,.2f} GB \nDiferencia: {diferencia:,.2f} GB")