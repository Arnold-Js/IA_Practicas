#Mejorar el ejercicio 15
import datetime
import random

Cliente = input("ingresa tu nombre: ")
nom_producto = input("ingresa el nombre del producto: ")
tienda = input("ingresa el nombre de la tienda: ")
folio = random.randint(1,100)
fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
total_compra = float(input("ingresa el total de tu compra: "))

if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print(f"============= TICKET DE COMPRA ============")
    print(f"Tienda: {tienda}")
    print(f"Folio: {folio}")
    print(f"fecha y hora: {fecha}")
    print(f"--------------------------------------------")
    print(f"cliente: {Cliente}")
    print(f"Producto: {nom_producto}")
    print(f"Total de la compra: {total_compra}")
    print(f"Descuento aplicado: {descuento}")
    print(f"total a Pagar: {total_final}")
    print(f"--------------------------------------------")
    print(f"¡Gracias por tu Compra! ¡Vuelva pronto!")
    print(f"===========================================")
    
else:
    print(f"============= TICKET DE COMPRA ============")
    print(f"Tienda: {tienda}")
    print(f"Folio: {folio}")
    print(f"fecha y hora: {fecha}")
    print(f"--------------------------------------------")
    print(f"cliente: {Cliente}")
    print(f"Producto: {nom_producto}")
    print(f"El total a pagar es: {total_compra} por la compra de {nom_producto}")
    print(f"--------------------------------------------")
    print(f"¡Gracias por tu Compra! ¡Vuelva pronto!")
    print(f"===========================================")