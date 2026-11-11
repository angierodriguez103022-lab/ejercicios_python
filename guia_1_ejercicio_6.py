# 6. Estimación de Presupuesto de Proyectos de Software: Una firma de desarrollo cobra sus proyectos según el esfuerzo de ingeniería. Solicita las horas estimadas de frontend, backend y QA, junto con el valor por hora estándar. Incluye un costo fijo obligatorio del 10% adicional por gestión de proyecto (PM). Muestra el desglose de horas y el costo total.
print("="*20, "ESTIMACIÓN DE PRESUPUESTO DE PROYECTOS DE SOFTWARE", "="*20)

horas_frontend = int(input("Ingrese las horas estimadas de frontend: "))
horas_backend = int(input("Ingrese las horas estimadas de backend: "))
horas_qa = int(input("Ingrese las horas estimadas de QA: "))
valor_hora_est = float(input("Ingrese el valor por hora estándar: "))

total_horas = horas_frontend + horas_backend + horas_qa
costo_base = total_horas * valor_hora_est
costo_pm = costo_base * 0.10
costo_total = costo_base + costo_pm

print("="*20, "DETALLE PRESUPUESTO", "="*20)
print(f"Horas estimadas de frontend: {horas_frontend:,.0f} \nHoras estimadas de backend: {horas_backend:,.0f} \nHoras estimadas de QA: {horas_qa:,.0f} \nCosto base: $ {costo_base:,.0f} \nCosto de gestión de proyecto (PM): $ {costo_pm:,.0f} \nCosto total por pagar corresponde a: $ {costo_total:,.0f}")