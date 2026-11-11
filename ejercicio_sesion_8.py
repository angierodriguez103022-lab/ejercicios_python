#Se desea reforestar un bosque cuya superficie se mide en hectáreas. Solicite al usuario la superficie del bosque en hectáreas y, según el tamaño, aplique la siguiente distribución en árboles:
# Superficie mayor a 1.000.000 m2: 70% pino | 20% oyamel | 10% cedro
# Sperficie menor o igual a 1.000.000 m2: 50% pino | 30% oyamel | 20% cedro
#Datos de densidad de siembra:
# En 10 m2 caben 8 pinos.
# En 15 m2 caben 15 oyameles.
# En 18 m2 caben 10 cedros.
# Una hectárea equivale a 10.000 m2.
# Salidas esperadas: número total de pinos, oyameles y cedros que se deben sembrar.

superficie = float(input("Ingrese la superficie del bosque en hectáreas: "))
hectarea_metros = 10000
superficie_metros = superficie * hectarea_metros

if superficie_metros > 1000000:
    pino = superficie_metros * 0.7
    oyamel = superficie_metros * 0.2
    cedro = superficie_metros * 0.1
else:
    pino = superficie_metros * 0.5
    oyamel = superficie_metros * 0.3
    cedro = superficie_metros * 0.2

total_pinos = pino / 10 * 8
total_oyamel = oyamel / 15 * 15
total_cedros = cedro / 18 * 10

print("-"*20,"DETALLE DE SIEMBRA", "-"*20 )
print(f"Total de superficie para pino: {pino:,.0f} M2, se deben sembrar {total_pinos:,.0f} pino(s) \nTotal de superficie para oyamel: {oyamel:,.0f} M2, se deben sembrar {total_oyamel:,.0f} oyamel(es), \nTotal de superficie para cedro: {cedro:,.0f} M2, se deben sembrar {total_cedros:,.0f} cedro(s)")