# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random



k = int(input('Введите натуральное число: '))
res = ''
x = "x"
deg = '**'
pl = ' + '
equ = ' = 0'

while k > 0:
    coef = random.randint(0, 101)
    if k == 1:
       coef = str(coef)
       res += coef + x
       coef = random.randint(1, 101)
       coef = str(coef)
       res += pl + coef  + equ
       print(res)
    else: 
        if coef == 0:
            pass
        elif coef == 1:
            res += pl + x + deg
        else:
            coef = str(coef)
            degree = str(k)
            res += coef + x + deg + degree + pl
            # print(i)
            # print(k)
            print(res)
    k -=1    
        
     

path = 'filetask4.txt'
with open (path, 'a') as poly:
    poly.write(res + '\n')

