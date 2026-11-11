#Pedir 4 notas  la nota 1 es te tarea  y corresponde al 30% del total de la nota
#La nota 2 es del examen 1 y corresponde al 20% de la nota final
#la nota 3 del examen 2  corresponde al 30% de la nota final
#La nota 4 de la tarea final coreesponde al 20% de la nota final.
#Mostrar el promedio 

#5.0+4.0+3.0+2.0=14/4

nota_uno = float(input("Ingrese la nota uno: "))
nota_dos = float(input("Ingrese la nota dos: "))
nota_tres = float(input("Ingrese la nota tres: "))
nota_cuatro = float(input("Ingrese la nota cuatro: "))

porcentaje_nota_uno = nota_uno * 0.30
porcentaje_nota_dos = nota_dos * 0.20
porcentaje_nota_tres = nota_tres * 0.30
porcentaje_nota_cuatro = nota_cuatro * 0.20

promedio_ponderado = porcentaje_nota_uno + porcentaje_nota_dos + porcentaje_nota_tres + porcentaje_nota_cuatro

print(f"El promedio ponderado corresponde a: {promedio_ponderado:,.1f}")