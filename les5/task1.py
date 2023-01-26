from random import randint as ri

total_sweet = 120
take_sweet = 0
player_sweet = 0
bot_sweet = 0

def start_game():
    print("На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.\n Первый ход делает человек.\n За один ход можно забрать не более чем 28 конфет.\nПобедитель - тот, кто оставил на столе 0 конфет.")
    who_is_firt() 

def who_is_firt():
    random_number = ri(1,2)
    if random_number == 1:
        plaeyr_turn()
    else:
        bot_turn()

def plaeyr_turn():
    global total_sweet
    global take_sweet
    global player_sweet
    print(f"Ваш ход, сейчас на столе {total_sweet} конфет")
    take_sweet = int(input("Сколько конфет вы берете?: "))
    while take_sweet>28 or take_sweet<0 or take_sweet>total_sweet:
        take_sweet = int(input("Вы берете слишком много конфет! Попробуйте ещё раз!"))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    if total_sweet > 0:
        bot_turn()
    else:
        print("Вы победили!")

def bot_turn():
    global total_sweet
    global take_sweet
    global bot_sweet
    take_sweet = total_sweet % 29 if total_sweet % 29 !=0 else ri(1,28)
    total_sweet-=take_sweet
    bot_sweet+= take_sweet
    print(f"Бот взял{take_sweet} конфет! на столе осталось {total_sweet} конфет")
    if total_sweet>0:
        plaeyr_turn()
    else:
        print("Бот победил!")
