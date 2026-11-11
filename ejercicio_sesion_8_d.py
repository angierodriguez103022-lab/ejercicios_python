# Una tienda virtual ofrece descuentos a sus clientes bajo ciertas condiciones. El descuento se aplica si el cliente realiza una compra superior a $ 50 dolares y además está registrado en la plataforma. También se otorga el descuento si el cliente tiene un cupón válido, sin importar el valor de la compra. El programa debe evaluar las condiciones y mostrar si el cliente recibe o no el descuento.

#compra > 50 registrado = si
#cupon = si
compra = float(input("Ingrese el valor de la compra: $"))
registrado_plataforma = input("¿Está registrado en la plataforma (Si/No)?: ")
cupo = input("¿Tiene un cupón válido (Si/No)?: ")

if (compra > 50 and registrado_plataforma == "Si") or cupo == "Si":
    print("El cliente recibe descuento en la compra")
else:
    print("El cliente no recibe descuento en la compra")