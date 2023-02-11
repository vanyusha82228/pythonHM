from stedent_database import set_stedent, set_rating


def add_student():
    metric = input("Введите данные(Фамилия, Имя, класс через пробел): ").split(' ')
    set_stedent(metric)

def put_rating():
    last_name = input("Введите фамилию: ")
    lesson = input("Название урока: ")
    rating = input("Введи оценку или оценки: ").split(' ')
    set_rating(last_name, lesson, rating)