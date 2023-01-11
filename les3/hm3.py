# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# # Пример:
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3]
# new_list = []
# for i in range(len(list)):
#     if i % 2 != 0:
#         new_list.append(list[i])
# print(new_list)

# def mult(new_list):
#     proizv = 0
#     for i in new_list:
#         proizv +=i
#     return proizv

# print(mult(new_list))



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# list = [2, 3, 4, 5, 6]
# result = []

# len_list = len(list)

# half_len= len_list/2
# if half_len %2 != 0:
#     half_len= int(half_len+1)

# for i in range(len_list):
#     if i< half_len:
#         result.append(list[i]*list[len_list-1-i])

# print(result)




# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


list = [1.1, 1.2, 3.1, 5, 10.01]

min = 1
max = 0

for i in list:
    if(i-int(i))<= min:
        min = i - int(i)
    if(i- int(i))>= max:
        max = i - int(i)

print(round(max-min, 2))

