def print_table(x, y):
    opciones_casillas = ["", "X", "0"]
    yoqse = [[[], [], []],
             [[], [], []],
             [[], [], []]]

    for i in x:
        yoqse[i[0]][i[1]] = opciones_casillas[1]

    for i in y:
        yoqse[i[0]][i[1]] = opciones_casillas[2]

    print(f'''
         {yoqse[0[0]]} | {yoqse[0[1]]} | {yoqse[0[2]]} 
        ---|---|---
         {yoqse[1[0]]} | {yoqse[1[1]]} | {yoqse[1[2]]} 
        ---|---|---
         {yoqse[2[0]]} | {yoqse[2[1]]} | {yoqse[2[2]]}
    ''')




