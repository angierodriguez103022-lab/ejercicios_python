# 9. Costeo de Importaciones y Aranceles (Landed Cost): Una compañía importa mercancía. Solicita el valor FOB en dólares, la tasa de cambio (TRM), el costo del flete internacional y el seguro. Calcula el valor CIF en moneda local, aplica un arancel del 10% sobre el CIF y muestra el costo total nacionalizado.
print("="*20, "COSTEO DE IMPORTACIONES Y ARANCELES (LANDED COST)", "="*20)

valor_fob = float(input("Ingrese el valor FOB: "))
flete = float(input("Ingrese el costo del flete internacional: "))
seguro = float(input("Ingrese el costo del seguro: "))
tasa_cambio = float(input("Ingrese la tasa de cambio (TRM): "))

cif = (valor_fob + flete + seguro) * tasa_cambio
arancel = cif * 0.10
costo_total_nacionalizado = cif + arancel

print("="*20, "DETALLE IMPORTACIONES Y ARANCELES", "="*20)
print(f"El valor FOB corresponde a: $ {valor_fob:,.0f} dolares \nEl costo del flete internacional corresponde a: $ {flete:,.0f} dolares \nEl costo del seguro corresponde a: $ {seguro:,.0f} dolares \nLa tasa de cambio corresponde a: $ {tasa_cambio:,.0f} pesos \nValor CIF en modena local: $ {cif:,.0f} pesos \nArancel del 10%: $ {arancel:,.0f} pesos \nEl costo total nacionalizado corresponde a: $ {costo_total_nacionalizado:,.0f} pesos")