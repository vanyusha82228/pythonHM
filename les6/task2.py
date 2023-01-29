# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

data = [12, "asf", 34534]

list_srt = list(filter(lambda x: type(x)== str, data))
nums = list(filter(lambda x: type(x)== int, data))
print(list_srt, nums, sep=",")