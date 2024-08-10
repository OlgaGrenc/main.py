n = int(input("Введите число от 3 до 20, (тогда приложение выдаст ключ из цифр, каждая пара которых либо дает в сумме ваше число, либо кратна ему)... "))
def rebus(n):
    add = []
    for i in range(1, 20):
        for j in range(1+i, 11):
            if n % (i+j) == 0:
                add.append(f'{i}{j}')
    result = ''.join(add)
    return result


result = rebus(n)
print(f'{n} - {result}')
