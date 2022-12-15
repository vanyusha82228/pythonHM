# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

numOfDay = int(input("Input number of day: "))

if numOfDay>5 and numOfDay<8:
    print("day off")
elif numOfDay<6 and numOfDay>0:
    print("Weekdays")
else:
    print("error")