# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# Святослав, задача конечно по твоей методике по семинару.
# Хочется решить конечно ее в общем виде для любого многочлена. Но пака голова плывет от кол-ва информации... ))

path = 'S02_2_hw5-1.txt'
with open(path, 'r') as d:
    data1 = d.readline()
data1 = data1.split()
data1 = [int(data1[0][:-3]), int(data1[1] + data1[2][:-1]), int(data1[3] + data1[4])]
print(data1)

path = 'S02_2_hw5-2.txt'
with open(path, 'r') as d:
    data2 = d.readline()
data2 = data2.split()
# print(data2)
data2 = [int(data2[0][:-3]), int(data2[1] + data2[2][:-1]), int(data2[3] + data2[4])]
print(data2)

data_res = []
for i in range(len(data1)):
    data_res.append(data1[i] + data2[i])

path = 'S02_2_hw5_result.txt'
with open(path, 'w') as d:
    data3 = d.writelines(f'{data_res[0]}x^2 + {data_res[1]}x + {data_res[2]} = 0')

# print (data_res)