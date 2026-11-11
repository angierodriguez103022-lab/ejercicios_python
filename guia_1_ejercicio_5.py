# 5. Cálculo de Nómina Básica (Devengados y Deducibles): Una empresa necesita calcular la liquidación mensual de un empleado. Solicita el valor del salario diario y los días trabajados en el mes. Calcula el salario bruto, resta un 4% para pensión y un 4% para salud sobre el bruto, e imprime el neto a pagar.
print("="*20, "CÁLCULO DE NÓMINA BÁSICA", "="*20,"\n")

salario_diario = float(input("Ingrese el valor del salario diario: "))
dias_trabajo = int(input("Ingrese los días trabajos al mes: "))

salario_bruto = salario_diario * dias_trabajo
pension = salario_bruto * 0.04
salud = salario_bruto * 0.04
#descuentos = salario_bruto - 0.08
neto_pagar = salario_bruto - pension - salud

print(f"El salario diario corresponde a: {salario_diario:,.0f} \nLos días trabajados en el mes corresponde a:{dias_trabajo:.0f} \nSalario bruto: {salario_bruto:,.0f} \nDescuentos por pensión: {pension:,.0f} \nDescuento por salud: {salud:,.0f} \nNeto a pagar corresponde a: {neto_pagar:,.0f}")