# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Если бы не пример выполнения, то задачу решил бы по другому :)

N = int(input('Please, enter the number: '))
listA = []

def Fact (n: int):
    factorial = 1
    if n >= 1:
        for ind in range (1, n + 1):
            factorial = factorial * ind
        return factorial
# print(Fact(3)) - проверка работы функции факториала ))

i = 1
while i <= N:
    listA.append(Fact(i))
    i += 1 

print(listA)