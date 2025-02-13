#ejercicios14: mostrar la calificacion por letra
nota = int(input("ingresa tu calificacion (0-100)"))

if 90 <= nota <= 100:
    print("tu calificacion es: 'A'")
elif 80 <= nota <= 90:
    print("Tu calificacion es: B")
elif 70 <= nota <= 80:
    print("Tu calificacion es: C")
elif 60 <= nota <= 70:
    print("Tu calificacion es: D")
else:
    print("Tu calificaion es: F")
