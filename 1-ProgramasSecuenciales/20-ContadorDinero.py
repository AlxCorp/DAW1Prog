#  20. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos
#  cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

e2 = int(input("Indica la cantidad de monedas de 2e que tienes: "))  # Pedimos las diferentes cantidades
e1 = int(input("Indica la cantidad de monedas de 1e que tienes: "))
cent50 = int(input("Indica la cantidad de monedas de 50cent que tienes: "))
cent20 = int(input("Indica la cantidad de monedas de 20cent que tienes: "))
cent10 = int(input("Indica la cantidad de monedas de 10cent que tienes: "))

e2 *= 100   # Convertimos todas las cantidades a céntimos
e1 *= 100
cent50 *= 50
cent20 *= 20
cent10 *= 10

dinero = e2 + e1 + cent50 + cent20 + cent10  # Sumamos todas las cantidades

euros = dinero // 100    # Parte entera para euros
centimos = dinero % 100  # Resto para céntimos

print("Tienes un total de", euros, "Euros y", centimos, "Céntimos")  # Imprimimos el Resultado
