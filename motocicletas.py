marca_moto = "Yamaha"
precio_moto = 5000
if marca_moto == "Honda":
    descuento = precio_moto * 0.05
elif marca_moto == "Yamaha":
    descuento = precio_moto * 0.08
elif marca_moto == "Suzuki":
    descuento = precio_moto * 0.10
else:
    descuento = precio_moto * 0.02

precio_a_pagar = precio_moto - descuento

print(f"El precio de la moto es: {precio_moto}")
print(f"El descuento aplicado es: {descuento}")
print(f"El precio a pagar es: {precio_a_pagar}")

marca_moto = input("Ingrese la marca de la moto: ")
precio_moto = 5000

if marca_moto == "Honda":
    descuento = precio_moto * 0.05
elif marca_moto == "Yamaha":
    descuento = precio_moto * 0.08
elif marca_moto == "Suzuki":
    descuento = precio_moto * 0.10
else:
    descuento = precio_moto * 0.02

precio_a_pagar = precio_moto - descuento

print(f"El precio de la moto es: {precio_moto}")
print(f"El descuento aplicado es: {descuento}")
print(f"El precio a pagar es: {precio_a_pagar}")