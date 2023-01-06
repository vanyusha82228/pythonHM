# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3]
new_list = []
for i in range(len(list)):
    if i % 2 != 0:
        new_list.append(list[i])
print(new_list)

def mult(new_list):
    proizv = 0
    for i in new_list:
        proizv +=i
    return proizv

print(mult(new_list))