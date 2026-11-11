# En una institución educativa se realizará un torneo académico exclusivo para estudiantes que cumplan ciertos requisitos. Para poder participar, el estudiante debe tener una nota promedio igual o superior a 4.0 y una asistencia mínima del 85%. Sin embargo, existe una excepción: si el estudiante ha ganado algún reconocimiento académico durante el año, puede participar aunque no cumpla uno de los dos requisitos anteriores. El sistema debe evaluar si el estudiante puede participar o no en el torneo según esta información. Se deben pedir los datos necesarios y mostrar un mensaje claro indicando si puede o no participar.
#promedio => 4.0
#asistencia => 85%

#reconocimiento == "si"
#asistencia => 85%
#promedio <= 4.0

#reconocimiento == "si"
#asistencia <= 85%
#promedio => 4.0

print("="*20, " TORNEO ACADÉMICO ", "="*20)
#3
promedio = float(input("Ingrese la nota promedio obtenida por el estudiante: "))
#0.5
asistencia = int(input("Ingrese la asistencia del estudiante de 1 a 100: "))/100
#Si
reconocimiento = input("¿Ha ganado algún reconocimiento académico durante el año (Si/No)?: ")
#                                                                    V
#                                         V                         and                V
#                     F                   or                V                          V
#           F      and         F          or                V       and           V    or            F      
if (promedio >= 4 and asistencia >= 0.85) or ( reconocimiento == "Si" and (promedio >= 4 or asistencia >= 0.85)
):
    print("El estudiante puede participar en el torneo")
else:
    print("El estudiante no puede participar en el torneo")