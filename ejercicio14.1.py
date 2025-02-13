#uso de la libreria datatime
import datetime

nombre = input("ingresa tu nombre: ")

fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Nombre del Cliente: {nombre} y la fecha y hora: {fecha}")
