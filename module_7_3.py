"""Домашнее задание по теме "Оператор "with".
Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП."""


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        signs = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_names in self.file_names:
            with open(file_names, "r", encoding='utf-8') as file:
                text = file.read().lower()
                for i in signs:
                    if i in text:
                        text.replace(i, '')
                    words = text.split()
                    all_words[file_names] = words
            return all_words

    def find(self, word):
        location = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                location[key] = value.index(word.lower()) + 1
        return location

    def count(self, word):
        all_ = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            all_[value] = words_count
        return all_


""" Пример выполнения программы:"""
finder2 = WordsFinder('test_file')
print(finder2.get_all_words())    # Все слова
print(finder2.find('TEXT'))     # 3 слово по счёту
print(finder2.count('teXT'))    # 4 слова teXT в тексте всего

"""Вывод на консоль:
{'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 
'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
{'test_file.txt': 3}
{'test_file.txt': 4}"""
