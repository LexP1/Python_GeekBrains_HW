# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from typing import List

num = int(input('Введите числа для перевода в двоичное: '))
result1 = num
list = []
while num >= 1:
    digit:int = num%2
    # print(f'{num}   {digit}')
    num = num // 2
    list.append(digit)
# print(list)
list.reverse()
result = ''.join(str(x) for x in list)
print(f'number {result1} in binary is {result}')