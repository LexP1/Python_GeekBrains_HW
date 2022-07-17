# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

num = int(input('Введите числа для соствления ряда Фибоначчи, в т.ч. для отрицательных чисел: '))
m_num = - num

listFibonacci = []
def fibonacciMinus (n):
    if n == -1: return 1
    elif n == -2: return -1
    return fibonacciMinus (n + 2) - fibonacciMinus (n + 1) 

def fibonacciPlus (n):
    if n == 0: return 0
    elif n == 0 or n == 1 or n == 2: return 1
    return fibonacciPlus(n-1) + fibonacciPlus(n-2)

for i in range(m_num, 0):
    listFibonacci.append(fibonacciMinus(i))
print (listFibonacci)

for i in range(0, num + 1):
    listFibonacci.append(fibonacciPlus(i))
print (listFibonacci)
