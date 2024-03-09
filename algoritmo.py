cantidad_camisas = 7
precio_unitario = 10
total_sin_descuento = cantidad_camisas * precio_unitario
if cantidad_camisas >= 6:
    total_a_pagar = total_sin_descuento * 0.8
else:
    total_a_pagar = total_sin_descuento * 0.9
print("El total a pagar por las camisas es:", total_a_pagar)

cantidad_camisas = int(input("Ingrese la cantidad de camisas: "))
precio_unitario = int(input("Ingrese el precio unitario: "))

total_sin_descuento = cantidad_camisas * precio_unitario

if cantidad_camisas >= 5:
    total_a_pagar = total_sin_descuento * 0.8
else:
    total_a_pagar = total_sin_descuento * 0.9

print("El total a pagar por las camisas es:", total_a_pagar)