"""Домашнее задание по теме "Блокировки и обработка ошибок"
Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.
Задача 'Банковские операции'"""


from threading import Thread, Lock
from random import randint
from time import sleep


class Bank(Thread):

    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        super().__init__()

    def deposit(self):

        for j in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            i = randint(50, 500)
            self.balance += i
            print(f"Пополнение: {i}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for j in range(100):
            i = randint(50, 500)
            print(f"Запрос на {i}")
            if self.balance > i:
                self.balance -= i
                print(f"Снятие: {i}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
                sleep(0.001)
        print(f"Итоговый баланс: {self.balance}")


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
