def action():
    print("Если вы хотите записать информацию в файлик введите 1 \n Если вы хотите хотите считать информаци введие 3 \n Если вы хотите выйти нажмите 3")
    choise = int(input())
    print()
    return choise

def db_view():
    print(f"В каком ввиде вы хотите считать данные?")
    print("Введите 1 для выбора:\nфамилия\nИмя\nТелефон\nОписание\n")
    print("Введите 2 для выбора:\nфамилия,Имя,Телефон,Описание\n")
    choise = int(input())
    print()
    return choise