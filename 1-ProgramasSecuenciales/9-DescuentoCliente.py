# 9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
# cuanto deberá pagar finalmente por su compra.

totalCompra = float(input("Indica el total de la compra: "))    # Pedimos el total
descuento = 0.85                                                # Declaramos el descuento

totalDescuento = totalCompra * descuento     # Aplicamos el descuento

print("El total de la compra es de", totalDescuento, "€")    # Imprimimos el resultado
