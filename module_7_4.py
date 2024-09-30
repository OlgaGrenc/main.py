"""Домашнее задание по теме "Форматирование строк".
Цель задания:

Освоить различные методы форматирования строк в Python.
Научиться применять эти методы в контексте описания соревнования. История: соперничество двух команд -
Мастера кода и Волшебники данных.
"""
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time)/tasks_total

"""
Использование %:

Переменные: количество участников первой команды (team1_num)."""
print("В команде Мастера кода участников: %(team1_num)s !" % {'team1_num': 6})

"""Переменные: количество участников в обеих командах (team1_num, team2_num)."""
print("Итого сегодня в командах участников: %(team1_num)d и %(team2_num)d !" % {'team1_num': 5, 'team2_num': 6})

"""Использование format():
Переменные: количество задач решённых командой 2 (score_2)."""
print("Команда Волшебники данных решила задач: {score_2} !".format(score_2=score_2))

"""Переменные: время за которое команда 2 решила задачи (team1_time)."""
print(" Волшебники данных решили задачи за {team1_time} c !".format(team1_time=team1_time))


"""Использование f-строк:
Переменные: количество решённых задач по командам: score_1, score_2"""

print(f'"Команды решили {score_1} и {score_2} задач.”')

"""Переменные: исход соревнования (challenge_result)."""


def defined_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = "Победа команды Мастера кода!"
        return result
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = "Победа команды Волшебники Данных!"
        return result
    else:
        result = "Ничья!"
        return result


challenge_result = defined_result()
print(f'Результат битвы: победа команды {challenge_result}!')

"""Пример итоговой строки: 'Результат битвы: победа команды {}!'"""

"""Переменные: количество задач (tasks_total) и среднее время решения (time_avg)."""

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")

"""Комментарии к заданию:
В русском языке окончания слов меняются (1 участник, 2 участника), пока что давайте не обращать на это внимания.
Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать.Например, для challenge_result"""

"""
alternative values:
score_1 = 40
score_2 = 42
tasks_total = 82
time_avg = 350.4
"""
