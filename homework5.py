# 2 part
immutable_var = 1, 2, 3
immutable_var = immutable_var + (4, [5, 6], "plus", False)
print(immutable_var)
immutable_var = immutable_var * 2
print(immutable_var)
print(immutable_var[0], immutable_var[4])
# 3 part
# переменная не может быть заменена по свойству неизменяемости элементов кортежа,
# выражение не будет выполнено:immutable_var [1] = 3
# 4 part
mutable_list = ["table", "desk", "chair", "pen", "paper"]
print(mutable_list)
print(mutable_list[0:2])
print(mutable_list[0:3:2])
mutable_list[0] = "chalk"
print(mutable_list)
mutable_list.remove("paper")
print(mutable_list)
mutable_list.append("book")
print(mutable_list)
mutable_list.extend(["pensil", "copybook"])
print(mutable_list)
print("list" in mutable_list)
print("list" not in mutable_list)
