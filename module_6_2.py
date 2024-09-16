"""Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."
Цели: Применить сокрытие атрибутов и повторить наследование.
Рассмотреть на примере объекта из реального мира.
"""


class Vehicle:
    __COLOR_VARIANTS = ["black", "green", "white", "red", "orange"]

    def __init__(self, owner: str, __model: str, __color: str, __engine_power: int):
        self.owner = owner
        self.__model = __model
        self.__engine_poweer = __engine_power
        self.__color = __color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_poweer}'

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model(), "\n", self.get_horsepower(),
              "\n", self.get_color(), "\n", f"Владелец {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() not in self.__COLOR_VARIANTS:
            print(f"Нельзя сменить цвет на {new_color}.")
        elif new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.upper()


class Sedan (Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

"""Вывод на консоль:
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: blue
Владелец: Fedos
Нельзя сменить цвет на Pink
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: BLACK
Владелец: Vasyok"""
