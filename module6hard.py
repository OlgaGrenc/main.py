class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = [1 for _ in range(self.sides_count)]
        self.__sides = list(sides)
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, b, g):
        if isinstance(r, int) and isinstance(b, int) and isinstance(g, int):
            if r in range(0, 255) and b in range(0, 255) and g in range(0, 255):
                return True
        return False

    def set_color(self, r, b, g):
        if self.__is_valid_color(r, b, g):
            self.__color = [r, b, g]

    def __is_valid_sides(self, *sides):
        for i in sides:
            if isinstance(i, int) and i > 0:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):     # возвращает периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = len(self) / (2*3.14)

    def get_square(self):
        self.__radius = 3.14*(self.__radius**2)   # площадь круга pr**2
        return self


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2
        return (p * (p - sides[0])*(p - sides[1])*(p - sides[2])) ** 0.5     # ф.Герона, степень 0.5=sqrt без имп.(=1/2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, *([sides] * self.sides_count))

    def get_volume(self):
        side_cube = self.get_sides()[0]
        volume = side_cube ** 3
        return volume


circle1 = Circle((200, 200, 100), 10)      # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)    # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)     # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)     # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)      # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
