'''
1. Напишите программу, удаляющую из файла все слова, содержащие "abc".

!!! У МЕНЯ В VISUAL STUDIO CODE ПРОБЛЕМЫ С КИРИЛЛИЦЕЙ, ПОЭТОМУ abc !!!
'''
# with open('www.txt', 'r') as data:
from random import randint
#string = data.readline()

string_text = "abc small shop is shop for  all abcgoods buyers"
substring = 'abc'
text_lst = string_text.split(" ")
print(text_lst)
output_txt = filter(lambda x: x.lower().find(substring) == -1, text_lst)
print(*output_txt)

with open('www.txt', 'w') as data:
    data.write("small shop is shop for all buyers")

"Shop abc is a shop of abcgoods things"
'''
2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"
'''
# 1. Вариант человек против человека:


def input_dat(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(
        f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)  # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

# 2.Вариант человек против бота c "интеллектом":


def input_dat(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(
        f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


def bot_calc(value):
    k = randint(1, 29)
    while value-k <= 28 and value > 29:
        k = randint(1, 29)
    return k


player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)  # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

'''
3. Создайте программу для игры в "Крестики-нолики".
Вариант интерфейса:
 1  |  2 | 3
--------------
 4  |  5 | 6
--------------
 7  |  8 | 9

'''

print('Игра "Kрестики нолики"')

board = list(range(1, 10))


def design_board(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)


def choice(tic_tac):
    valid = False
    while not valid:
        player_index = input('Ваш ход, выберите ячейку ' + tic_tac + ' --> ')
        try:
            player_index = int(player_index)
        except:
            print('Что то не то нажали')
            continue
        if player_index >= 1 and player_index <= 9:
            if (str(board[player_index-1]) not in 'XO'):
                board[player_index-1] = tic_tac
                valid = True
            else:
                print('Занято')
        else:
            print('Попробуйте ещё раз')


def victory_check(board):
    victory = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
               (0, 3, 6), (1, 4, 7), (2, 5, 8),
               (0, 4, 8), (2, 4, 6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def game(board):
    counter = 0
    vic = False
    while not vic:
        design_board(board)
        if counter % 2 == 0:
            choice('X')
        else:
            choice('0')
        counter += 1
        if counter > 4:
            tt_win = victory_check(board)
            if tt_win:
                print(tt_win, 'Победа')
                vic = True
                break
            if counter == 9:
                print('Победила, ДРУЖБА)')
        design_board(board)


game(board)


'''
4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff
'''

with open('encode.txt', 'w') as data:
    data.write('aaaasssdddwwwwwwwwwwwweeeffffff')

with open('encode.txt', 'r') as data:
    string = data.readline()


def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string


with open('encode.txt', 'r') as file:
    decoded_string = file.read()

with open('decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + rle_encode(decoded_string))
print(
    f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')

'''

5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.
*Пример:* 

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

'''
lst = [1, 5, 2, 3, 4, 6, 1, 7]
res = []
i = 0
k = 0
for j, item in enumerate(lst):
    res.append([item])
    print(res)
    for i in range(j, len(lst)):
        if lst[i] > res[j][k]:
            res[j].append(lst[i])
            k += 1
    k = 0
print(res)
