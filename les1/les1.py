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

# x = int(input("input x: "))
# y = int(input("input y: "))

# if x>0 and y>0:
#     print("first quarter")
# elif x<0 and y>0:
#     print("second quarter")
# elif x<0 and Y<0:
#     print("third quarter")
# elif x>0 and y<0:
#     print("fourth quarter")
# else:
#     print("error")



#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# x = int(input("enter quarter number: "))


# if x==1:
#     print(f"by x from 0 to plus infinity", f"by y from 0 to plus infinity", sep="\n")
# elif x==2:
#     print(f"by x from 0 to minus infinity", f"by y from 0 to plus infinity", sep="\n")
# elif x==3:
#     print(f"by x from 0 to minus infinity", f"by y from 0 to minus infinity", sep="\n")
# elif x==4:
#     print(f"by x from 0 to plus infinity", f"by y from 0 to minus infinity", sep="\n")
# else:
#     print("error")


#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

xA = int(input("enter the x coordinate of the first point: "))
yA = int(input("enter the y coordinate of the first point: "))
xB = int(input("enter the x coordinate of the second point: "))
yB = int(input("enter the y coordinate of the second point: "))

print(f"Distance between points ({xA},{yA}) and ({xB},{yB}) is {round(((xA-xB)**2 + (yA-yB)**2)**0.5, 3)}")