grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# grades by alphabet
# students are in a random order
# right decision: {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
s = students
print("Количество учеников(по алфавиту) ", len(grades))
print("Количество оценок каждого ", len(grades[0]), len(grades[1]), len(grades[2]), len(grades[3]), len(grades[4]))
print("Общий балл каждого ученика ", sum(grades[0]), sum(grades[1]), sum(grades[2]), sum(grades[3]), sum(grades[4]))
a = sum(grades[0]) / len(grades[0])
b = sum(grades[1]) / len(grades[1])
c = sum(grades[2]) / len(grades[2])
d = sum(grades[3]) / len(grades[3])
e = sum(grades[4]) / len(grades[4])
#print (list(s))
s = list(s)
# print((s[0], s[1], s[2], s[3], s[4]))
print('Список учащихся по алфавиту:')
z = min(s[0], s[1], s[2], s[3], s[4])
print(z)
s.remove('Aaron')
y = min(s[0], s[1], s[2], s[3])
print(y)
s.remove('Bilbo')
x = min(s[0], s[1], s[2])
print(x)
s.remove('Johnny')
w = min(s[0], s[1])
print(w)
s.remove('Khendrik')
v = min(s)
print(v)
average_grade = {z:a, y:b, x:c, w:d, v:e}
print("Средний балл ", average_grade)
