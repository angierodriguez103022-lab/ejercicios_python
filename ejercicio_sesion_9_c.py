usuario = input("Ingrese el usuario: ")


if usuario == "pepe":
    clave = input("Ingrese la clave: ")
    if clave == "123":
        print("Bienvenido!!!")
    else:
        print("Clave incorrecta")
else:
    print("Usuario incorrecto")