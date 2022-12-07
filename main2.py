'''
1 Напишите программу, которая принимает на вход вещественное число и 
показывает сумму его цифр.
*Пример:*

- 6782 -> 23
- 0.56 -> 11

'''
num = input('Введите число: ')
str_num = str(num)  # число в строку
str_num = str_num.replace('.', '')  # производим замену десятичного разделителя
lst_str = list(str_num)  # строку с числом в список строк с цифрами
lst_num = map(int, lst_str)  # преобразовываем каждый элемент полученного
# списка строк с цифрами в список целых чисел
print(sum(lst_num))  # применяем функцию `sum()`


'''
2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
Запрещено использовать функцию factorial из библиотеки math

'''

N = int(input('Введите число: '))

result = 1  # переменная, где хранится результат
for i in range(1, N + 1):
    result *= i
print(result)


'''
3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
*Пример:*

- Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)
'''

N = int(input('Введите число: '))

lst = []
for i in range(1, N + 1):
    lst.append((1 + (1 / i))**i)
print(sum(lst))

'''
4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции вводятся с клавиатуры.

'''

N = int(input('Введите число: '))
lst = list(range(-N, N + 1))

print(lst)
a = int(input('Введите номер элемента списка a: '))
b = int(input('Введите номер элемента списка b: '))
print(lst[a] * lst[b])


'''
5 Реализуйте алгоритм перемешивания списка.
Из библиотеки random использовать можно только randint

'''

s = int(input('Введите количество элементов списка: '))
s = list(range(1, s + 1))
print('Исходный список: ', s)
p = [0 for _ in s]
i = 1
res = []

while i < len(s):
    if p[i] < i:
        j = 0 if i % 2 == 0 else p[i]
        s[i], s[j] = s[j], s[i]
        p[i] += 1
        i = 1
        if s not in res:
            res.append(list(s))
    else:
        p[i] = 0
        i += 1

print('Все возможные случайные варианты: ', res)
