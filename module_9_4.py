import random
# В версии Python 3.12 ошибка для импорта: from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
l_func = map(lambda x, y: x == y, first, second)
print(list(l_func))
print("\n" * 1)   # ввод пробелов в консоль


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "a", encoding="UTF-8") as file:
            for i in data_set:
                file.write(f'{i}\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# __call__ makes functions


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
"""Примерный результат (может отличаться из-за случайности выбора):
Да
Да
Наверное"""
