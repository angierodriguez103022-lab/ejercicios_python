# Un pintor cotiza un trabajo. El programa pide el largo, ancho y alto de la habitación, y el rendimiento de la pintura (m2 por galón) y su precio. Calcula el área de las cuatro paredes, los galones necesarios y el costo total.

largo_habitacion = float(print("Ingrese el largo de la habitación: "))
ancho_habitacion = float(print("Ingrese el ancho de la habitación: "))
alto_habitacion = float(print("Ingrese el alto de la habitación: "))
rend_pintura = float(print("Ingrese el rendimiento de la pintura (m2 por galón): "))
precio_pintura = float(print("Ingrese el precio de la pintura: "))

area = 2 * (largo_habitacion * alto_habitacion) + 2 * (ancho_habitacion * alto_habitacion)
calcular_galones = area / rend_pintura
costo_total = calcular_galones * precio_pintura

print("Area:", area)
print("Galones: ", calcular_galones)
print("Costo total: ", costo_total)