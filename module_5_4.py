"""В классе House создайте атрибут houses_history = [],
который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта,
тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
а также значение атрибута houses_history.
"""


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args)
        for i in cls.houses_history:
            print(i[:])
        return object.__new__(cls)
#
    ''' def __new__(cls, *args, **kwargs):
        __arg = None
        cls.houses_history.append(args)
        for i in cls.houses_history:
            print(i[:])
        if cls.__arg is None:
            cls.__arg = super().__new__(cls)
        return cls.__arg'''

    def __init__(self, *args, **kwargs):
        self.args = args

    def __del__(self):
        return f'{self.args} снесён, но он останется в истории'


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
""" Тебуемый
Вывод на консоль:
['ЖК Эльбрус']
['ЖК Эльбрус', 'ЖК Акация']
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Акация снесён, но он останется в истории
ЖК Матрёшки снесён, но он останется в истории
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Эльбрус снесён, но он останется в истории
"""
