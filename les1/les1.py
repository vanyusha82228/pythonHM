# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

# numOfDay = int(input("Input number of day: "))

# if numOfDay>5 and numOfDay<8:
#     print("day off")
# elif numOfDay<6 and numOfDay>0:
#     print("Weekdays")
# else:
#     print("error")


# # Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = int(input("input x: "))
y = int(input("input y: "))

if x>0 and y>0:
    print("first quarter")
elif x<0 and y>0:
    print("second quarter")
elif x<0 and Y<0:
    print("third quarter")
elif x>0 and y<0:
    print("fourth quarter")
else:
    print("error")