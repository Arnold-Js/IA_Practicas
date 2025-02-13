import math
#Ejercicio 7 Calcular el Area de un Circulo
radio = float(input("introduce el radio del circulo en metros:\n"))

area = math.pi * (radio ** 2)
print(f"El Area del circulo con radio {radio} metros es: {area:.2f} metros cuadrados\n")