# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# path = 

my_list = [1, 3, 4, 1, 3, 6, 9, 9, 3, 10]

res_list = []
for i in range(len(my_list)):
    count = 0
    for index in my_list:
        if my_list[i] == index: count +=1
    if count == 1: res_list.append(my_list[i])
 
print(res_list)