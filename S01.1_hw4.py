# Написать программу, которая принимает на вход номер четверти и выдает диапазон координат.

quarter = int(input("Введите номер четверти системы координат: "))

if quarter == 1:
    print("Координаты в четверти: x > 0 и y > 0")
elif quarter == 2:
    print("Координаты в четверти: x < 0 и y > 0")
elif quarter == 3:
    print("Координаты в четверти: x < 0 и y < 0")
elif quarter == 4:
    print("Координаты в четверти: x > 0 и y < 0")
else:
    print("Вы ввели неверное число. Диапазон должен быть от 1 до 4")

# Как вернутся на 3 строку коду после 14 строки кода для повторного ввода?