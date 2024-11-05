"""Домашнее задание по теме 'Многопроцессное программирование'
Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.
Задача 'Многопроцессное считывание'"""
import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, "r") as f:
        while True:
            line = f.readline()
            all_data.append(line)
            if not line:
                break


if __name__ == "__main__":
    filenames = list(f'./file {number}.txt' for number in range(1, 5))

    # линейный вызов:
    start_ = time.time()

    def line_call():
        for file in filenames:
            read_info(file)


    line_call()
    end = time.time()
    print(f"Линейный вызов:{end - start_}")

    # многопроцессорный вызов:
    start_1 = time.time()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end_1 = time.time()
    print(f'Многопроцессорный вызов:{end_1 - start_1}')
