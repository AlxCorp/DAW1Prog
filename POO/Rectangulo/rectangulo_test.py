from POO.Point.point import Point
from rectangulo import Rectangle

p1 = Point(0, 4)
p2 = Point(5, 7)

r = Rectangle(p1, p2)

print(r.area)
print(r.perimetro)