# Задача 4*. Создайте игру в крестики-нолики.
# from pickletools import markobject
print('4. Крестики - нолики (2 игрока)')

game_field = list(range(1,10))

def Print_field(game_field: list):
    print(f'{game_field[0]:^3}|{game_field[1]:^3}|{game_field[2]:^3}')  # :^3  ^ - по центру, ост - отступы по 3 знака
    print('----------')
    print(f'{game_field[3]:^3}|{game_field[4]:^3}|{game_field[5]:^3}')
    print('----------')
    print(f'{game_field[6]:^3}|{game_field[7]:^3}|{game_field[8]:^3}')
    print('----------')

# Можно было кратко:
#   print("-" * 10)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 10)


# Print_field(game_field)
# player_field = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
# enemy_field = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]

# def Player_turn(game_field: list, mark):
#     while True:
#         move = int(input('Игрок1, сделайте ваш ход: '))
#         if 10 > move > 0 and game_field[move+1].isdigit():
#             game_field[move+1] = mark
#             break
#         else:
#             print('Эта клетка занята, попробуйте выбрать другую :)')


game_field = list(range(1,10))

def take_input(player_symbol):
   valid = False
   while not valid:
      player_answer = input(f'Куда поставим {player_symbol}? ')
      try:
         player_answer = int(player_answer)
      except:
         print('Некорректный ввод. Вы уверены, что ввели число?')
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(game_field[player_answer-1]) not in 'XO'):
            game_field[player_answer-1] = player_symbol
            valid = True
         else:
            print('Эта клетка уже занята!')
      else:
        print('Некорректный ввод. Введите число от 1 до 9.')

def check_win(game_field):
   win_code = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_code:
       if game_field[each[0]] == game_field[each[1]] == game_field[each[2]]:
          return game_field[each[0]]
   return False

def main(game_field):
    counter = 0
    win = False
    while not win:
        Print_field(game_field)
        if counter % 2 == 0:
           take_input('X')
        else:
           take_input('O')
        counter += 1
        if counter > 4:
           symbol = check_win(game_field)
           if symbol:
              print(f'{symbol} выиграл!')
              win = True
              break
        if counter == 9:
            print('Ничья!')
            break
    Print_field(game_field)

main(game_field)

input('Нажмите Enter для выхода')