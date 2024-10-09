"""Домашнее задание по теме "Итераторы"
Цель: освоить механизмы работы итераторов и описания методов __next__ и __iter__.
Закрепить навык создания и выбрасывания исключений."""


class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration()
        if self.step < 0 and self.pointer < self.stop:
            raise StopIteration()
        else:
            self.i = self.pointer
            self.pointer += self.step
            return self.i


# Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')

"""Вывод на консоль:
Шаг указан неверно
-5 -4 -3 -2 -1 0 1
6 8 10 12 14
5 4 3 2 1
"""