"""Домашнее задание по теме "Множественное наследование"""


class Horse:

    x_distance = 0
    sound_ = "Frrr"

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0
    sound = "I train, eat, sleep and repeat"

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


# Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

"""Вывод на консоль:
(0, 0)
(10, 15)
(5, 35)
I train, eat, sleep, and repeat"""
