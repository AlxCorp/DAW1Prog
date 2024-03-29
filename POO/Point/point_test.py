"""Implementa una clase Point con sus atributos x e y. La clase debe contener: su constructor, los getters y setters
(propiedades), un invert_coordinates() que invierta las coordenadas x e y del punto. Además, la clase debe tener un
__str__() para poder imprimir los puntos en formato “(x, y)”.
Implementa un test donde crees un punto, lo imprimas utilizando de manera implícita el método __str__(), imprimas su
coordenada x, asignes 0 a su coordenada x, y vuelvas a imprimir el punto. """

from point import Point

p = Point(1, 2)
print(p.__str__())
print(p.x)
p.x = 0
print(p.__str__())
