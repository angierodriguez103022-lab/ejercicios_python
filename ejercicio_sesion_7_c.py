# Ejercicio 2. Aprobación de un examen
# Solicite la calificación obtenida por un alumno en un examen (en escala de 0 a 10). El programa debe imprimir el mensaje "Aprobado" si la calificación es mayor a 8, y "Reprobado" en caso contrario.
print("="*20, " APROBACIÓN DE UN EXÁMEN ", "="*20)

nota_alumno = float(input("Ingrese la calificación obtenida en el exámen (en escala de 0 a 10):"))

if nota_alumno > 8:
    print("Aprobado")
else:
    print("Reprobado")