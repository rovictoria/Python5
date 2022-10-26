# Задача 4*. Создайте игру в крестики-нолики.

game_field = [1,2,3,4,5,6,7,8,9]
def Print_field(game_field):
    print(f'{game_field[0]}^3|{game_field[1]}^3|{game_field[2]}^3')
    print('----------')
    print(f'{game_field[3]}^3|{game_field[4]}^3|{game_field[5]}^3')
    print('----------')
    print(f'{game_field[6]}^3|{game_field[7]}^3|{game_field[8]}^3')
    print('----------')

Print_field(game_field)
