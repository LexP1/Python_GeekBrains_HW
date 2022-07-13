# Реализуйте алгоритм перемешивания списка

# вариант 1 резерв идея

def shuffle(list_A: list):
    list_B = list_A[:]
    for i in range (0, len(list_B)):
        from random import randint
        j = randint(0, len(list_A) - 1)
        # print(f'j={j}')
        list_B[i] = list_A[j]
        del list_A[j]
        # print(list_B)
        # print(list_A)
    return list_B

list = ['Александр', 'Анна', 'Федор', 'Агата', 'Мирон']
print(list)
print(shuffle(list))

# 3 вариант

# def shuffle(list_A: list, list_B: list):
#     if i == 0: return
#     else:   
#         list_B = []
#         for i in list_A:
#             from random import randint
#             temp = list_A[randint(0, len(list_A) - 1)]
#             list_B.append(temp)
#             for i in list_B:
#                 if list_B[i] == temp: shuffle(list_A, list_B)
#         return list_B

# list_1 = [2, 'b', 'c', 'hello']
# list_2 = []
# print(shuffle(list_1, list_2))


# 2 так себе, но работает криво

# def mix(list_A: list, list_B: list):
    
#     list_B = []
#     for i in list_A:
#         print(len(list_A))
#         from random import randint
#         j = randint(0, len(list_A) - 1)
#         print(j)
#         list_B.append(list_A[j])
#         del list_A[j]
#         print(list_A)
#         print(list_B)

#     return list_B

# list_1 = [2, 'b', 'c', 'hello']
# list_2 = []
# print(mix(list_1, list_2))

