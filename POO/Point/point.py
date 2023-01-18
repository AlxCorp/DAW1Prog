class Point:
    def __init__(self, x: float, y: float):
        self.__z = None
        self.__x: float = x
        self.__y: float = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def __str__(self):
        print(f'({self.__x},{self.__y})')

    def invert_coordinates(self):
        self.__z = self.__x
        self.__x = self.__y
        self.__y = self.__z
