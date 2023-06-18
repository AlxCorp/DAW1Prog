# 8. Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber
#  cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total
#  que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

salario = float(input("Indica el salario base: "))                          # Pedimos los datos de entrada
venta1 = 0.1 * float(input("Indica el importe de la primera venta: "))
venta2 = 0.1 * float(input("Indica el importe de la segunda venta: "))
venta3 = 0.1 * float(input("Indica el importe de la tercera venta: "))

sueldo = round(salario + venta1 + venta2 + venta3, 2)       # Realizamos el cálculo total

print("El sueldo total será de: ", sueldo, "€")     # Imprimimos el resultado
