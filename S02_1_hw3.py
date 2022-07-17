# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# 1.1 1.2 3.1 5 10.01

numbers = input('Введите числа для массива через пробел: ')
print('\n')
list = numbers.split()
print('list = ', list)

listB = []
for i in range(len(list)):
    temp = float(list[i]) - int(float(list[i]))
    listB.append(temp)
print(listB)

for i in range(len(listB)):
    max = min = listB[0]
    if listB[i] > max: max = listB[i]
    if listB[i] < min: min = listB[i]
    print(f'{i})', type(i))
    print(f'max = {max}', type(max))
    print(f'min = {min}', type(min))
# print(f'max = {max}')
# print(f'min = {min}')


result = round((max - min), 2)
print(result)