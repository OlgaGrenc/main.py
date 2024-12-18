import requests
import numpy as np
import pandas as pd
import random


from threading import Thread  #для мультипоточности по requests

# help(requests) # общая информация
print("\n'Библиотека requests'")
r = requests.get('https://www.python.org')
print("r.status_code:", r.status_code)
# print("r.text :", r.text)
print("r.headers['content-type'] :", r.headers['content-type'])
print("b'Python is a programming language' in r.content :", b'Python is a programming language' in r.content)
print("")
r = requests.get('https://requests.readthedocs.io/en/latest/index.html')
r.encoding = 'utf-8'

"""
Requests - это элегантная и простая HTTP-библиотека для Python, созданная для Людей. В настоящее время вы 
просматриваете документацию Релиз в разработке.

#Полезные ссылки (на сайте)
Быстрый старт
Расширенное использование
Справочник по API
История релизов
Руководство для авторов
Рекомендуемые пакеты и расширения
Запросы @ GitHub
Запросы @ PyPI
Баг-трекер
Содержание
Быстрый старт
Оставить заявку
Передача параметров в URL
Содержание ответа
Содержимое двоичного отклика
Содержимое ответа JSON
Содержимое необработанного отклика
Пользовательские заголовки
Более сложные POST-запросы
POST файл, закодированный в составной части
Коды состояния ответа
Заголовки ответов
Печенье
Перенаправление и история
Времени ожидания
Ошибки и исключения"""
# раскомментировав код до конца комментария можно получить информацию с сайта в виде ссылок по библиотеке requests


def a():

    #with open('filename.txt', 'wb') as fl:
        #for note in r.iter_content(chunk_size=128):
            #fl.write(note)
            # подобно print(r.read)
       pass


the_first = Thread(target=a)
the_second = Thread(target=a)
the_third = Thread(target=a)
the_fourth = Thread(target=a)

the_first.start()
the_second.start()
the_third.start()
the_fourth.start()
the_first.join()
the_second.join()
the_third.join()
the_fourth.join()

def http_error():
    match r.status_code:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 200:
            return "Ok"
        case _:
            return "Something's wrong with the internet"


f = http_error()
print(f)

"""pandas -считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
numpy -создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль."""
#print(help(pd))  #общая информация, основные методы и запросы, адрес url библиотеки с полным описанием
print("\n'Библиотека pandas'")
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s)
print(s.index)

# Данные, которые необходимо записать в файл
names = ["Иван", "Анна", "Сергей", "Ольга", "Максим"]
ages = [32, 28, 45, 39, 27]
cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Краснодар", "Екатеринбург"]

# Создание заголовков
header = "name,age,city\n"

# Открытие файла для записи
with open('data.txt', 'w', encoding='utf-8') as file:
    # Запись заголовков
    file.write(header)

    # Цикл для записи данных построчно
    for i in range(len(names)):
        line = f"{names[i]},{ages[i]},{cities[i]}\n"
        file.write(line)


# Чтение данных из текстового файла
df = pd.read_csv('data.txt')

# Просмотр первых пяти строк таблицы
print("\nПервые пять строк:")
print(df.head())

# Количество записей в таблице
num_records = len(df)
print(f"\nКоличество записей: {num_records}")

# Средний возраст людей
avg_age = df['age'].mean()
print(f"\nСредний возраст: {avg_age:.2f} лет")

# Список уникальных городов
unique_cities = df['city'].unique()
print("\nУникальные города:")
for city in unique_cities:
    print(city)

# Фильтрация данных по возрасту (старше 35 лет)
filtered_df = df.query("age > 35")
print("\nЛюди старше 35 лет:")
print(filtered_df)

"""Библиотека numpy
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль."""
#print(help(np)) # общая информация, основные методы и запросы, адрес url библиотеки с полным описанием
print("\n'Библиотека numpy'")
# Создаем массив чисел от 1 до 10
array = np.arange(1, 11)
print("Исходный массив:", array)

# Выполняем математическую операцию (например, умножение каждого элемента на 2)
result = array * 2
print("Результат умножения элементов на 2:", result)

# Еще одна операция (например, возведение каждого элемента в квадрат)
squared_result = array ** 2
print("Квадраты элементов:", squared_result)
