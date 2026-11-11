# En un juego de preguntas a las que se responde Si o No gana quien responda correctamente las tres preguntas.
# Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
#  ¿Colon descubrió América?
#  ¿La independencia de México fue en el año 1810?
#  ¿The Doors fue un grupo de rock Americano?

pregunta_1 = "¿Colón descubrió América?"
pregunta_2 = "¿La independencia de México fue en el año 1810? (Si/No)"
pregunta_3 = "¿The Doors fue un grupo de rock Americano? (Si/No)"

print(pregunta_1)
respuesta_1 = input("Responda Si o No: ").lower()

if respuesta_1 == "si":
        print(pregunta_2)
        respuesta_2 = input("Responda Si o No: ").lower()
        if respuesta_2 == "si":
            print(pregunta_3)
            respuesta_3 =  input("Responda Si o No: ").lower()
            if respuesta_3 == "si":
                print("Correcto, haz ganado el juego")
        else:
            print("Respuesta incorrecta, fin del juego")
else:
    print("Respuesta incorrecta, fin del juego")