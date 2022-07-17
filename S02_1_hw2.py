# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math

numbers = input('Введите числа для массива через пробел: ')
print('\n')
list = numbers.split()
print('list = ', list)

listB = []
for i in range(math.ceil(len(list)/2)):
    listB.append(int(list[i]) * int(list[-i - 1]))
print(listB)