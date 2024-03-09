sueldo = 1700
if sueldo <= 1000:
    descuento = sueldo * 0.1
elif sueldo <= 2000:
    descuento = (1000 * 0.1) + ((sueldo - 1000) * 0.05)
else:
    descuento = (1000 * 0.1) + (1000 * 0.05) + ((sueldo - 2000) * 0.03)
sueldo_neto = sueldo - descuento
print("El descuento es:", descuento)
print("El sueldo neto que recibe el trabajador es:", sueldo_neto)

sueldo = float(input("Ingrese el sueldo: "))

if sueldo <= 1000:
    descuento = sueldo * 0.1
elif sueldo <= 2000:
    descuento = (1000 * 0.1) + ((sueldo - 1000) * 0.05)
else:
    descuento = (1000 * 0.1) + (1000 * 0.05) + ((sueldo - 2000) * 0.03)

sueldo_neto = sueldo - descuento

print("El descuento es:", descuento)
print("El sueldo neto que recibe el trabajador es:", sueldo_neto)