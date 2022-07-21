# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число для вывода списка простых множителей этого числа: '))

def prime_number (param: int):
    for i in range(2, param):
        if (param % i) == 0: return False
    return True

def prime_number_list (param1: int):
    list = []
    for i in range(2, param1):
        if prime_number(i) == True:
            list.append(i)
    return list

def find_dividers (param2: int, listA: list):
    list = []
    for i in listA:
        if param2 % i == 0:
            list.append(i)
    return list

list_of_primes = prime_number_list(number)
# print(list_of_primes)
list_of_dividors = find_dividers(number, list_of_primes)
print(list_of_dividors)


# отработка темы семинара по записи в файл
path = 'S02_2_hw2_result.txt'
with open (path, 'w+') as data:
    data.writelines(f'Делителями числа {number} являются следющие простые множители\n{list_of_dividors}')













exit()

#{KFV!

# def fill_primeN ()
for i in range(2, number):
    primeNumbers.append(prime_Number(i))


print(primeNumbers)

for i in range(primeNumbers):
    if number % i == 0:
        listAprime.append(i)

path = 'S02_2_hw2_result.txt'
with open (path, 'w') as data:
    data.writelines(f'Делителями числа {number} являются следющие простые множители\n{listAprime}')

exit()
for i in range (1, 10):
    if number % i == 0:
        listA.append(i)

print(listA) # для проверки, что лист множителей сформирован
# отработка темы семинара по записи в файл
path = 'S02_2_hw2_result.txt'
with open (path, 'w+') as data:
    data.writelines(f'Делителями числа {number} являются следющие простые множители\n{listA}')

