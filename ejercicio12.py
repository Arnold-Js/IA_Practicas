#ejercicios12: Adivinar un numero
import random
numero_aleatorio = random.randint(1,10)
adivina = int(input("Adivina el numero entre 1 y 10: "))

print(f"El numero aleatorio es {numero_aleatorio}.")
if adivina == numero_aleatorio:
    print("¡Correcto! has adivinado el numero.")
else:
    print(f"Incirrecto. El numero era {numero_aleatorio}.")
