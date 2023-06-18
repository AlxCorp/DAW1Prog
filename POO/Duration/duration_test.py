from duration import Duration

t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.
print(t1)
t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.
print(t2)
t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2
print(t3)
