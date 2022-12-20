# 1) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# n = int(input("input n: "))

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return fact(n-1)*n

# list = []

# for i in range(1,n+1):
#     list.append(fact(i))

# print(list)



# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5


# n = int(input("input n: "))

# for i  in range(2,n+1):
#     if n % i==0:
#         print(i)
#         break
    

#  Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]   


# n = abs(int(input("Input n: ")))


# numberOfIndex = 5
# listOfIndex =[]
# for i in range(numberOfIndex):
#     listOfIndex.append(int(input(f'Enter the {i+1} element: ')))
# print(listOfIndex)

# list = []
# for i in range(-n,n+1):
#     list.append(i)
# print(list)
# res = 1
# for i in listOfIndex:
#     res*= list[i]

# print(f"answer: {res}")

# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.


n = abs(int(input("inpyt n: ")))
sum=0

for i in range(1,n+1):
    if i%2==0:
        sum=sum+i

print(sum)