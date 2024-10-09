"""Домашнее задание по теме "Генераторные сборки"
Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов."""

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
# first_result1 = list(zip(first, second))
f_r = (len(x) - len(y) if len(x) > len(y) else len(x) - len(y) for x, y in list(zip(first, second)) if len(x) != len(y))
first_result = f_r
print(list(first_result))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))
