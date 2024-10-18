"""Домашнее задание по теме "Потоки на классах"
Цель: научиться создавать классы наследованные от класса Thread.
Задача "За честь и отвагу!":"""
from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        self.name_of_knights = name
        self.power = power
        super().__init__()

    def run(self):
        print(f"{self.name_of_knights}, на нас напали!")
        value_of_enemies = 100
        day = 0
        while value_of_enemies:
            day += 1
            value_of_enemies -= self.power
            print(f"{self.name_of_knights} сражается {day} день, осталось {value_of_enemies} воинов!")
            sleep(1)
        print(f"{self.name_of_knights} одержал победу спустя {day} дней!")


first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Goland", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
