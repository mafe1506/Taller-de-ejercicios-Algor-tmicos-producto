num1 = 2
num2 = 4
num3 = 7
if num1 != num2 and num2 != num3 and num1 != num3:
    maximo = max(num1, num2, num3)
    print("El número mayor es:", maximo)
else:
    print("Los números no son distintos")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 != num2 and num2 != num3 and num1 != num3:
    maximo = max(num1, num2, num3)
    print("El número mayor es:", maximo)
else:
    print("Los números no son distintos")