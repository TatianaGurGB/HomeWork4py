# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

from tabnanny import check


path = 'filetask3.txt'
with open (path, 'r') as f:
    data = f.read()
print(data)
# print(type(data))

my_list = []
for i in data:
    check = False
    for j in my_list:
        if i == j: 
            check = True
    if check == False:
        my_list.append(i)
print(my_list)


# Читерство:
# my_list = [1,2,2,6,4,4,8,9,3,1]
# my_set = set(my_list)
# print(my_set)