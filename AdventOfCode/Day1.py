with open('Day1input.txt') as f:
    lines = f.readlines()

cleaned_lines = []

for n in lines:
    if n == "\n":
        cleaned_lines.append(n)
    else:
        cleaned_lines.append(n.replace("\n", ""))

suma_calorias = []
temp = 0
for i in lines:
    if i == "\n":
        suma_calorias.append(temp)
        temp = 0
    else:
        temp += int(i)

suma_calorias.sort(reverse=True)

print(suma_calorias)

calorias_3_maximos = 0
for h in range(3):
    calorias_3_maximos += suma_calorias[h]

print(calorias_3_maximos)
