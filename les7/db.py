def data_colector():
    s_name = input("Фамилия: ")
    f_name = input("Имя: ")
    tele = input("Телефон:")
    comment = input("Описание:")
    print()
    data = [s_name, f_name, tele, comment]
    return data

def db_save(data):
    file = "file.colum.txt"
    with open(file, "a") as data:
        data.write(f"Фамилия: {data[0]}; Имя:{data[1]}; Номер:{data[2]}; Описание: {data[3]}\n")
    
    file = "file_strok.txt"
    with open(file, 'a') as data:
        data.write(f"Фамилия: {data[0]};\n Имя:{data[1]};\n Номер:{data[2]};\n Описание: {data[3]}\n")

def db_print(choise):
    if choise == 1:
        with open("file_colum.txt", "r") as file:
            for line in  file:
                print(line, ens="")
    if choise == 2:
        with open("file_strok.txt", "r") as file:
            for line in  file:
                print(line, ens="")