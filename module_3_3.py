# Задача "Распаковка":
# 1.Функция с параметрами по умолчанию.
def print_params(a=1, b='строка', c=True, *params):
    print(a, b, c, *params)


print_params(3, 'программа', True, 9, 10)   # использование переменного числа позиционных параметров
# позволяет расширить переданные параметры функции
print_params()
print_params(b=25)   # функция принимает это значение; вывод: 1 25 True ; но ожидает другой тип данных - "str".
print_params(c=[1, 2, 3])   # функция принимает это значение; вывод: 1 строка [1, 2, 3];
# но ожидает другой тип данных -"bool".
print()  # разделитель заданий

# 2.Распаковка параметров (из списка и из словаря).
values_list = [2, 'str', False]
values_dict = {'a': True, 'b': 8, 'c': 'Hello'}
print_params(*values_list)
print_params(**values_dict)
print()  # разделитель заданий

# 3.Распаковка + отдельные параметры
# Создан список values_list_2 с двумя элементами разных типов
# Проверено, работает ли print_params(*values_list_2, 42).
values_list_2 = ['finish', True]
print_params(*values_list_2, 42)  # функция работает; вывод: finish True 42
