# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = list(input('Enter the number please: '))
if n < 0:
    n = -n
if ',' in n:
    n.remove(',')
sum: int = 0
for i in range (0, len(n)):
    sum += int(n[i])
print(f"The sum of digits in number is {sum}")