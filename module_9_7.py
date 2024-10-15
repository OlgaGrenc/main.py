"""Домашнее задание по теме "Декораторы"
Задание: Декораторы в Python
Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию."""


def is_prime(f):
    def wrapper(*variables):
        decoration = f(*variables)
        prime = True
        for i in range(2, int(decoration/2)+1):
            if decoration % i == 0:
                prime = False
        if prime == True:
            print('Простое')
        else:
            print("Составное")
        return decoration
    return wrapper


@is_prime
def sum_three(*variables):
    for i in variables:
        var = sum(variables)
    return var


result = sum_three(2, 3, 6)
print(result)
