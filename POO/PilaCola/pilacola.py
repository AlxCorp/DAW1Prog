"""
Clase que representa una estructura de datos tipo Pila(Stack) y tipo Cola(Queue).
    - Crear con o sin valores a través de otra
    - Obtener tamaño
    - Saber si está vacía
    - Vaciarla
    - Apilar/Encolar
    - Desapilar/Descolar
    - Leer último/primer elemento

Author: Alejandro Priego Izquierdo
Date: 10-02-2023
"""


class Stack:

    def __init__(self, *initial_input):
        self.__storage = []

        if self.__objects_from_input_stack(initial_input) != "exit":
            self.__storage.append(self.__objects_from_input_stack(initial_input))
        else:
            self.storage = initial_input

    # noinspection PyMethodMayBeStatic
    def __objects_from_input_stack(self, stack):
        if len(stack) == 1 and isinstance(stack[0], Stack):
            temp_objects = []
            for n in range(stack[0].size):
                temp_objects.append(stack[0].pop())
            return temp_objects
        return "exit"

    @property
    def storage(self):
        return self.__storage

    @storage.setter
    def storage(self, *input_objects):
        if input_objects:
            self.__storage.extend(input_objects)

    @property
    def size(self):
        return len(self.__storage)

    @property
    def is_used(self):
        return self.size != 0

    def empty(self):
        self.__storage.clear()
        return 'Pila vaciada con éxito!'

    def push(self, element):
        self.__storage.insert(0, element)
        return 'Elemento añadido con éxito!'

    def pop(self):
        return self.__storage.pop(0)

    @property
    def top(self):
        if self.is_used:
            return self.__storage[0]
        return 'La pila se encuentra vacía'


class Queue:

    def __init__(self, *initial_input):
        self.__storage = []

        if self.__objects_from_input_queue(initial_input) != "exit":
            self.__storage.append(self.__objects_from_input_queue(initial_input))
        else:
            self.storage = initial_input

    # noinspection PyMethodMayBeStatic
    def __objects_from_input_queue(self, queue):
        if len(queue) == 1 and isinstance(queue[0], Queue):
            temp_objects = []
            for n in range(queue[0].size):
                temp_objects.append(queue[0].dequeue())
            return temp_objects
        return "exit"

    @property
    def storage(self):
        return self.__storage

    @storage.setter
    def storage(self, *input_objects):
        if input_objects:
            self.__storage.extend(input_objects)

    @property
    def size(self):
        return len(self.__storage)

    @property
    def is_used(self):
        return len(self.__storage) != 0

    def empty(self):
        self.__storage.clear()
        return 'Cola vaciada con éxito!'

    def enqueue(self, element):
        self.__storage.append(element)
        return 'Elemento añadido con éxito!'

    def dequeue(self):
        return self.__storage.pop(0)

    @property
    def front(self):
        if self.is_used:
            return self.__storage[0]
        return 'La cola se encuentra vacía'
