#Mejorar el ejercicio 15
nombre = input("ingresa tu nombre: ")
nom_producto = input("ingresa el nombre del producto: ")

total_compra = float(input("ingresa el total de tu compra: "))
if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print(f"¡Felicidades! {nombre} Tienes un descuento del 10% en la compra de {nom_producto}. El total a pagar es: {total_final}")
else:
    print(f"El total a pagar es: {total_compra} por la compra de {nom_producto}")