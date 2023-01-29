#  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

num = input("Веведите вещественное число: ")

digs_sum = sum(map(int, filter(lambda el: el.isdigit(), num)))

print(digs_sum)