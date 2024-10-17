from threading import Thread
# import requests
from time import sleep
from datetime import datetime


time_start = datetime.now()


def write_words(word_count, file_name):
    with open(file_name, "a", encoding="UTF-8") as file:
        for i in range(1, word_count+1):
            file.write(f"Какое-то слово № {i}\n")
        sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


write_words(10, 'Example1.txt')
write_words(30, "Example2.txt")
write_words(200, "Example3.txt")
write_words(100, "Example4.txt")
time_end = datetime.now()
time_res = time_end - time_start
print("Работа потоков", time_res)
the_first = Thread(target=write_words, args=(10, "Example5.txt"))
the_second = Thread(target=write_words, args=(30, "Example6.txt"))
the_third = Thread(target=write_words, args=(200, "Example7.txt"))
the_fourth = Thread(target=write_words, args=(100, "Example8.txt"))
the_first.start()
the_second.start()
the_third.start()
the_fourth.start()
the_first.join()
the_second.join()
the_third.join()
the_fourth.join()
time_end1 = datetime.now()
time_res1 = time_end1 - time_end
print("Работа потоков", time_res1)
