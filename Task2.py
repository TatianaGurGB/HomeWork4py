# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.

from importlib.resources import path


num = int(input('Введите натуральное число: '))
pro = int(num/2)
my_list = []

if num % 2 == 0:
    my_list.append(2)
for i in range(3,pro+1,2):
    if num % i == 0:
        if (i == 3 or i == 5 or i ==7):
            my_list.append(i)
        elif (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
            pass
        else:
            my_list.append(i)

print(my_list)

