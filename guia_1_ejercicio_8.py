# 8. Análisis de Punto de Equilibrio: El departamento financiero desea determinar el volumen de ventas necesario para no tener pérdidas. Pide los costos fijos totales, el precio de venta unitario y el costo variable unitario. Calcula el margen de contribución y las unidades necesarias para el punto de equilibrio: Unidades = Costos Fijos / (Precio Venta - Costo Variable).
print("="*20, "ANÁLISIS DE PUNTO DE EQUILIBRIO", "="*20)
costo_fijo_total = float(input("Ingrese el costo fijo total: "))
precio_venta_unitario = float(input("Ingrese el precio de venta unitario: "))
costo_variable_unitario = float(input("Ingrese el costo variable unitario: "))

contribucion = precio_venta_unitario - costo_variable_unitario
unidades = costo_fijo_total / contribucion

print("="*20, "DETALLE PUNTO DE EQUILIBRIO", "="*20)
print(f"El costo fijo total corresponde a: $ {costo_fijo_total:,.0f} \nEl precio de venta unitario corresponde a: $ {precio_venta_unitario:,.0f} \nEl costo variable unitario corresponde a: $ {costo_variable_unitario:,.0f} \nMargen de contribución: $ {contribucion:,.0f} \nLas unidades necesarias para el punto de equilibrio corresponde a: {unidades:,.0f}")