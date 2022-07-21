# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# Ну и задачка, никогда так число Пи не разбирал... от рядов Лейбница, простых чисел, формулы Чудновского
# приходу к формуле Дэвид Бэйли, Питер Борвайн и Саймон Плафф копаясь которой все равно шло округление
# и в итоге прихожу к правильному заданию типа decimal и его точности prec...
# https://docs.python.org/3.7/library/decimal.html#decimal.prec

from decimal import Decimal, getcontext

num = int(input('Введите показатель точности для указания числа Пи: '))

getcontext().prec = num
number = Decimal(0)
for i in range(num):
    a = Decimal(1) / (16 ** i)
    b = Decimal(4) / (8 * i + 1)
    c = Decimal(2) / (8 * i + 4)
    d = Decimal(1) / (8 * i + 5)
    e = Decimal(1) / (8 * i + 6)
    element = a * (b - c - d - e)
    number += element
print(f'Число Пи с точностью {10 ** -num} равно {number}')









exit()

# find = str(round(number, k))
# print(find)
# print(find[-1])
# print(f'{listA[-1]} + {listA[-2]} = {listA[-1] + listA[-2]}')
# listB = []
# for i in range(len(listA)):
#     print(listA[-i])
#     listB[i] = listA[-i] + listA[-i - 1]
#
#     print(listB[i])

# print(listB.reverse())
    # print(find_digit[i + 2])



exit()
# https://docs.python.org/3.7/library/decimal.html#decimal.getcontext
import time
from decimal import Decimal, getcontext

def compute(n):
    # getcontext().prec = n
    res = Decimal(0)
    for i in range(n):
        a = Decimal(1)/(16**i)
        b = Decimal(4)/(8*i+1)
        c = Decimal(2)/(8*i+4)
        d = Decimal(1)/(8*i+5)
        e = Decimal(1)/(8*i+6)
        r = a*(b-c-d-e)
        res += r
    return res

# if __name__ == "__main__":
#     t1 = time.time()
res = compute(1000)
    # dt = time.time()-t1
print(res)
# print(dt)



exit()
def factorial_reg(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def pi_chud (precision):
    pi = 0.0
    # precision = 1
    for i in range (0, precision):
        pi = ((-1 ** i) * factorial_reg(6 * i) * (13591409 + 545140134 * i)) / ((factorial_reg(3 * i) * factorial_reg(i) ** 3) * ((640320 ** 3) ** (i + 1/2)))
    return 1/(12 *pi)

list = pi_chud(4)
print(list)









exit()

k = 5
listA = []
number = 0
for i in range (k):
    digit = (16 ** -i) * ((4 / (8 * i + 1)) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
    # print(digit)
    # listA.append(digit)
    number += digit #накапливаем математическую точность числ
print(listA)
print(number)
find = str(round(number, k))
print(find)
print(find[-1])
print(f'{listA[-1]} + {listA[-2]} = {listA[-1] + listA[-2]}')
# listB = []
# for i in range(len(listA)):
#     print(listA[-i])
#     listB[i] = listA[-i] + listA[-i - 1]
#
#     print(listB[i])

# print(listB.reverse())
    # print(find_digit[i + 2])




exit()

# Решение номер НОЛЬ

# использование ряда Лейбница
# 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13

print(f'4/1 - 4/3 = {4/1 - 4/3}')
print(f'4/1 - 4/3 + 4/5 - 4/7 = {4/1 - 4/3 + 4/5 - 4/7}')
print(f'4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 = {4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11}')
print(f'4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 - 4/15 = {4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 - 4/15}')



# Решение номер РАЗ - тривиальное
num = int(input('Введите показатель точности для указания числа Пи: '))
print(f'Число Пи с точностью {10 ** -num} равно {round(pi_chud(), num)}')

def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

start_time = time.time()
print(fact(10))
print(time.time() - start_time)

# решение номер ДВА
# вариант по Дэвид Бэйли, Питер Борвайн и Саймон Плафф
# ищем каждый знак в отдельности; набираем в списак; потом сращиваем

k = 100
listA = []
# number = 0
for i in range (k):
    digit = (16 ** -i) * ((4 / (8 * i + 1)) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
    # number += digit
    listA.append(digit)

listB = listA[0:3]
print(listB)
listB[0] = listB[0] - 3
print(listB[0])
result = 0
for i in range(len(listB)):
    result += listB[i]
    print(i)

print(result)

# print(''.join(map(str, list)))


