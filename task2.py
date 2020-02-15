'''
2. Напишите программу для игры “Камень-ножницы-бумага” для 2-их человек.
Правила:
• Ножницы бьют бумагу
• Бумага бьёт камень
• Камень бьёт ножницы
Игра должна продолжаться до 3-х побед. По окончании партии выводится победитель.
Подсказка
infinite loop
break
while
'''

import random


def game_mode(mode):
    mod_number = mode
    while 1:
        
        if mod_number == 1000:
            break
        elif mod_number > 2:
            mod_number = int(input('''Пожалуйста выберите режим 1 (vs компьютера) или режим 2 (vs игрок):
для выхода из игры напишите "1000" :'''))
        elif mod_number == 1:
            mod_number = 1
            break
        elif mod_number == 2:
            mod_number = 2
            break
    return mod_number




def game_with_comp():
    hodi = {1: "камень", 2: "ножницы", 3: "бумага"}
    i=0   #очки игрока
    j=0   #очки компа
    while 1:
        if i == 3:
            print(f"Поздравляем, вы выиграли игру у компьютера со счетом {i}:{j}")
            break
        elif j == 3:
            print (f"К сожалению Вы проиграли, ваш счет составил {i}:{j}")
            break
        player = int(input(''' 
1.камень
2.ножницы
3.бумага 
Ваш ход:'''))
        if 0 > player >= 3:
            while 1:
                player = int(input('''
1.камень
2.ножницы
3.бумага
Ваш ход: '''))
                if 0 < player <=3:
                    break
                
        vibor_comp = random.randint(1,3)
        
        if player == vibor_comp:
            print(f"НИЧЬЯ {hodi[player]} vs {hodi[vibor_comp]}")
        elif player == 1: 
            if vibor_comp == 2:
                i+=1
                print(f"Вы выйграли, ваш счет {i}:{j}")
            elif vibor_comp == 3:
                j+=1
                print(f"Вы проиграли, ваш счет {i}:{j}")
        elif player == 2:
            if vibor_comp == 3:
                i+=1
                print(f"Вы выйграли, ваш счет {i}:{j}")
            elif vibor_comp == 1:
                j+=1
                print(f"Вы проиграли, ваш счет {i}:{j}")
        elif player == 3:
            if vibor_comp == 1:
                i+=1
                print(f"Вы выйграли, ваш счет {i}:{j}")
            elif vibor_comp == 2:
                j+=1
                print(f"Вы проиграли, ваш счет {i}:{j}")




def game_with_player():
    hodi = {1: "камень", 2: "ножницы", 3: "бумага"}
    i=0   #очки игрока
    j=0   #очки игрока 2
    while 1:
        if i == 3:
            print(f"Поздравляем, игрок 1 выиграл со счетом {i}:{j}")
            break
        elif j == 3:
            print (f"Поздравляем, игрок 2 выйграл со счётом {i}:{j}")
            break
        
        
        while 1:
            player = int(input(''' 
1.камень
2.ножницы
3.бумага 
ход 1-го игрока:'''))
            if 0 > player >= 3:
                player = int(input('''
1.камень
2.ножницы
3.бумага
ход 1-го игрока: '''))
            elif 0 < player <=3:
                break
        while 1:        
            player_2 = int(input(''' 
1.камень
2.ножницы
3.бумага 
ход 2-го игрока:'''))
            if 0 > player_2 >= 3:
                player_2 = int(input('''
1.камень
2.ножницы
3.бумага
ход 2-го игрока: '''))
            elif 0 < player_2 <=3:
                break

        if player == player_2:
            print(f"НИЧЬЯ {hodi[player]} vs {hodi[player_2]}")
        elif player == 1: 
            if player_2 == 2:
                i+=1
                print(f"игрок 1 выйграл, счет {i}:{j}")
            elif player_2 == 3:
                j+=1
                print(f"игрок 2 выйрал, счет {i}:{j}")
        elif player == 2:
            if player_2 == 3:
                i+=1
                print(f"игрок 1 выйграл, счет {i}:{j}")
            elif player_2 == 1:
                j+=1
                print(f"игрок 2 выйрал, счет {i}:{j}")
        elif player == 3:
            if player_2 == 1:
                i+=1
                print(f"игрок 1 выйграл, счет {i}:{j}")
            elif player_2 == 2:
                j+=1
                print(f"игрок 2 выйрал, счет {i}:{j}")






vibor_mod = int(input(''' 
1. игрок vs компьютера 
2. игрок vs игрока
выберите режим игры:'''))
mode_selected = game_mode(vibor_mod)
if mode_selected == 1:
    game_with_comp()
if mode_selected == 2:
    game_with_player()