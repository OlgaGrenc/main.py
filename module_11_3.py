import inspect
import sys
from pprint import pprint

"""Интроспекция"""


def introspection_info(obj):
    """Верните словарь или строки с данными об объекте, включающий следующую информацию:
        - Тип объекта.
        - Атрибуты объекта.
        - Методы объекта.
        - Модуль, к которому объект принадлежит.
        - Другие интересные свойства объекта, учитывая его тип (по желанию).
    Примерный вывод: {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...],
     'module': 'builtins', 'other': '...'}."""
    info_attr = []
    methods_ = []
    for i in dir(obj):
        if i.startswith('__') and i.endswith('__'):
            methods_.append(i)
        elif i != i.startswith('__') and i != i.endswith('__'):
            info_attr.append(i)
    is_func = inspect.isfunction(introspection_info)
    info_f = inspect.getmodule(introspection_info)
    doc = inspect.getdoc(introspection_info)
    version_ = sys.version
    vers = sys.version_info
    argv_ = sys.argv
    print('documentation:', doc, '\n', 'type:(arg in obj)', type(obj), '\n', 'attributes:', info_attr, '\n',
          'methods:', methods_, '\n', 'module:', introspection_info.__module__, '\n', 'is_func:', is_func, '\n',
          'argv:', argv_, '\n', 'path to module:', info_f, '\n', 'version:', version_, '\n', 'version_info:', vers,
          '\n', 'builtins in module:', __builtins__)
    pprint(dir(__builtins__))


number_info = introspection_info(42)
# print("Интроспекция в агрументах и методах для функции:")
# pprint(dir(introspection_info))
