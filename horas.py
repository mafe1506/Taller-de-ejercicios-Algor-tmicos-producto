horas_trabajadas = 50
tarifa_por_hora = 11
if horas_trabajadas > 48:
    salario = 40 * tarifa_por_hora + (horas_trabajadas - 50) * (tarifa_por_hora * 1.5)
else:
    salario = horas_trabajadas * tarifa_por_hora
print("El salario del trabajador es:", salario)

horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
tarifa_por_hora = int(input("Ingrese la tarifa por hora: "))

if horas_trabajadas > 50:
    salario = 40 * tarifa_por_hora + (horas_trabajadas - 50) * (tarifa_por_hora * 1.5)
else:
    salario = horas_trabajadas * tarifa_por_hora

print("El salario del trabajador es:", salario)