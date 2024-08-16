# Функция составила новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот root_word содержит одно из этих слов.
# После функция вернула список same_words в качестве результата своей работы.
def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    other_words_ = []
    for i in other_words:
        other_words_.append(i.lower())
    for k in other_words_:
        if root_word in k:
            same_words.append(k)
    for j in other_words_:
        if j in root_word and root_word == "disablement":
            same_words.append(j.title())
        elif j in root_word:
            same_words.append(j)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
