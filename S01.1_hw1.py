# Напишите программу, которая принимает на вход цифру обозначающую день недели, и проверяет, является ли день выходным.

n = int(input('Введите число обозначающее день недели: '))
if n <= 0 or n >= 8:
    print("Дня недели с таким порядковым номером не существует")
# Разобрать проверку на дурака с повторным вводом чсла и запуском цикла. Возможно через цикл While?
elif n >= 1 and n <=5:
    print("Увы! Это день недели, но не выходной :)")
else:
    print("Ура! Это выходной день!")
    