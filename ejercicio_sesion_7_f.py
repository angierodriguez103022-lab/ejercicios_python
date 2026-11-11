
numero_materia = int(input("Ingrese la cantidad de materias: "))
promedio = float(input("Ingrese el promedio: "))
total_colegitura = numero_materia * 50

if promedio >= 9:
    descuento = total_colegitura * 0.30
    total_pagar = total_colegitura - descuento
else:
    iva = total_colegitura * 0.10
    total_pagar = total_colegitura + iva

print(f"El número de materias corresponde a: {numero_materia:,.0f} \nTotal por pagar: ${total_pagar:,.0f}")