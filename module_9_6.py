"""Домашнее задание по теме "Генераторы"
Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python."""
print("Первый вариант, без импорта itertools")


def all_variants(text):
    for i in range(len(text)):
        yield text[i]
    for i in range(len(text) - 1):
        yield text[i]+text[i-2]
    for i in range(len(text) - 2):
        yield text[i] + text[i - 2] + text[i-1]


a = all_variants("abc")
for i in a:
    print(i)

print("\nВторой вариант, c импортом itertools")
from itertools import combinations
    

def all_variants(text: str):
    for i in range(len(text)+1):
        for j in combinations(text, i):
            yield "".join(j)


a = all_variants("abc")
for i in a:
    print(i)
