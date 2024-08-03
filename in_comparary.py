try:
    first = int(input("Введите первое целое число: "))
except ValueError:
    first = int(input('Вводите внимательно! Введите целое число! '))
second = int(input("Введите второе целое число: "))
third = int(input("Введите третье целое число: "))
if first == second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
elif first != second != third:
    print("0")
elif input() != int(input()):
    print('Внимательно прочтите условие!')
print("Спасибо. Проведена обработка данных. Программа завершена.")
