"""Домашнее задание по теме "Try и Except"."""


def add_everything_up(a, b):
    try:
        c = float(a) + float(b)
    except TypeError:
        return f'{str(a)}{str(b)}'
    except ValueError:  # (except ValueError as exs:)
        # print(f"Ошибка {exs}, параметры ошибки {exs.args}")
        return f'{str(a)}{str(b)}'
    else:
        return float(round(c, 3))


print(add_everything_up(123.456, "строка"))
print(add_everything_up("яблоко", 42.15))
print(add_everything_up(123.456, 7))
