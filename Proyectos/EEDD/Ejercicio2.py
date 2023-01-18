class Usuario:
    def __init__(self, dni, nombre, apellidos, direccion):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion

    def usuario_info(self):
        return f'DNI: {self.dni}\n Nombre: {self.nombre}\n Apellidos: {self.apellidos}\n Dirección: {self.direccion}'


encontrado = False
lista_usuarios = [Usuario('123', 'Nombre1', 'Apellidos1', 'Mikasa1'),
                  Usuario('456', 'Nombre4', 'Apellidos4', 'Mikasa4'),
                  Usuario('789', 'Nombre7', 'Apellidos7', 'Mikasa7')]
print('Ya está creado los tres objetos:')

while True:
    dni = input('Introduce DNI a buscar: ')
    for i in range(0, len(lista_usuarios), 1):
        if lista_usuarios[i].dni == dni:
            print(lista_usuarios[i].usuario_info())
            encontrado = True
    if not encontrado:
        print('No se corresponde con ningún usuario')
    c = input('¿Quieres buscar otro usuario? (S/n): ')
    if (c != 's') and (c != 'S'):
        break
