# Домашняя работа по уроку "Пространство имен."
def test_function():
    # global inner_function
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_ = test_function()
# inner = inner_function()
"""- inner_function - функция не может быть вызвана,
т.к. находится в локальной области зачений объемлющей функции test_function; 
для возможности вызова inner_function, можно передать ей глобальное значение, 
убрав # в строчке 3 и для возможности вызова убать также и в строчке 10 -в данном примере"""
# print(test_)
# print(inner)
