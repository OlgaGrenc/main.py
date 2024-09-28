"""Позиционирование в файле. Метод tell"""
info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]


def custom_write(file_name, strings):
    strings_position = {}
    number = 1
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        strings_position[(number, file.tell())] = string
        file.write(string + '\n')
        number += 1
    file.close()
    return strings_position


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


""" Вывод на консоль:
 ((1, 0), 'Text for tell.')
 ((2, 16), 'Используйте кодировку utf-8.')
 ((3, 66), 'Because there are 2 languages!')
 ((4, 98), 'Спасибо!')"""

"""Пример полученного словаря:
{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
Где:
1, 2 - номера записанных строк.
0, 16 - номера байт, на которых началась запись строк.
'Text for tell.', 'Используйте кодировку utf-8.' - сами строки."""
