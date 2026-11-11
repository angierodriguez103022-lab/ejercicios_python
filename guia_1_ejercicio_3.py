# 3. Cálculo de Promedio Académico: Solicita al usuario las notas de tres evaluaciones de una asignatura y sus respectivos nombres. El programa debe calcular y mostrar el promedio aritmético simple de las tres calificaciones.
nota_evaluacion_uno = float(input("Ingrese la nota de la primera evaluación: "))
nombre_evaluacion_uno = input("Ingrese el nombre de la primera evaluación: ")

nota_evaluacion_dos = float(input("Ingrese la nota de la segunda evaluación: "))
nombre_evaluacion_dos = input("Ingrese el nombre de la segunda evaluación: ")

nota_evaluacion_tres = float(input("Ingrese la nota de la tercera evaluación: "))
nombre_evaluacion_tres = input("Ingrese el nombre de la tercera evaluación: ")

promedio = nota_evaluacion_uno + nota_evaluacion_dos + nota_evaluacion_tres / 3

print("-"*40)
print(f"Evaluación 1: {nombre_evaluacion_uno} | {nota_evaluacion_uno:.1f} \nEvaluación 2: {nombre_evaluacion_dos} | {nota_evaluacion_dos:.1f} \nEvaluación 3: {nombre_evaluacion_tres} | {nota_evaluacion_tres:.1f}")
print(f"El promedio aritmético simple de las  notas registras, corresponde a: {promedio:.1f}")