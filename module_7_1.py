'''Домашнее задание по теме "Режимы открытия файлов"
Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.

Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.'''
class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = str(weight)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, 'r')
        a = file.read()
        file.close()
        return a

    def add(self, *product):
        for i in product:
            if i.name not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(f'{str(i)} \n')
                file.close()
            elif i.weight == i.weight in self.get_products():
                print(f'Продукт {i} уже есть в магазине')
            elif True:
                file = open(self.__file_name, 'a')
                file.write(f'{str(i)} \n')
                file.close()
                continue


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

'''Вывод на консоль:
Первый запуск:
Spaghetti, 3.4, Groceries
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables

Второй запуск:
Spaghetti, 3.4, Groceries
Продукт Potato, 50.5, Vegetables уже есть в магазине
Продукт Spaghetti, 3.4, Groceries уже есть в магазине
Продукт Potato, 5.5, Vegetables уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables'''