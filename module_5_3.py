""""Перегрузка операторов.
Цель: применить знания о перегрузке арифметических операторов и операторов сравнения."""


class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def __str__(self):
        return f'Название {self.name}, количество этажей {self.numbers_of_floors}'
# 1 метод __eq__

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors
#  методы __lt__, __le__, __gt__, __ge__, __ne__

    def __lt__(self, other):
        return self.numbers_of_floors < other.numbers_of_floors

    def __le__(self, other):
        return self.numbers_of_floors <= other.numbers_of_floors

    def __gt__(self, other):
        return self.numbers_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        return self.numbers_of_floors >= other.numbers_of_floors

    def __ne__(self, other):
        return self.numbers_of_floors != other.numbers_of_floors
# 3 метод __add__

    def __add__(self, value):
        self.numbers_of_floors += value
        return self
# 4 методы __radd__, __iadd__

    def __radd__(self, value):
        self.numbers_of_floors += value
        return self

    def __iadd__(self, value):
        self.numbers_of_floors += value
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)    # __eq__

h1 = h1 + 10   # __add__
print(h1)
print(h1 == h2)

h1 += 10    # __iadd__
print(h1)

h2 = 10 + h2    # __radd__
print(h2)

print(h1 > h2)    # __gt__
print(h1 >= h2)   # __ge__
print(h1 < h2)    # __lt__
print(h1 <= h2)    # __le__
print(h1 != h2)   # __ne__
