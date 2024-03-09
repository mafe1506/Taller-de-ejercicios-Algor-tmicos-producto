precio_moto = float(input("Ingrese el precio de la moto: "))
dia_compra = input("Ingrese el día de la compra (martes, sábado, feriado): ")

if dia_compra == "martes":
    descuento = precio_moto * 0.12
elif dia_compra == "sábado":
    descuento = precio_moto * 0.18
elif dia_compra == "feriado":
    descuento = precio_moto * 0.25
else:
    descuento = 0

precio_a_pagar = precio_moto - descuento

print(f"El precio a pagar el día {dia_compra} es: {precio_a_pagar}")