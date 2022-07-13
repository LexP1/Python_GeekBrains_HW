# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число N: '))
i = -N
list = []

while i <= N:
    list.append(i) 
    i += 1

print(list)

first = int(input('Please enter the first element in List: '))
second = int(input('Please enter the second element in List: '))

def multiply (param_1, param_2):
    result = list[param_1] * list[param_2]
    return result

print(multiply(first, second))