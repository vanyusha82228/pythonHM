# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ round())

# import math

# x = float('{:.4f}'.format(math.pi))

# print(x)


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7


# n = int(input("Input n: "))

# i = 2 
# list =[]
# while i*i<=n:
#     while n%i== 0:
#         list.append(i)
#         n=n/i
#     i+=1
#     if n>1:
#         list.append(n)

# print(list)



# Задайте последовательность чисел. Напишите программу, которая выведет список элементов, которые не имели повторов в исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1


# import random

# list= []
# for x in range(1, 10):
#     list.append(random.randint(1, 10))

# print(list)
# my_list=[]

# for i in list:
#     if list.count(i) == 1:
#         my_list.append(i)

# print(my_list)




# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 
# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
#     a, b, c, d, e, h - рандом



import random as rand


def get_polynomial(pow):
    string = ''

    for i in range(pow, 1, -1):
        string += str(rand.randint(1, 99)) + 'x^' + str(i) + ' + '

    return string + str(rand.randint(1, 99)) + 'x + ' + str(rand.randint(1, 99))


k = int(input('Введите степень: '))
print(get_polynomial(k))