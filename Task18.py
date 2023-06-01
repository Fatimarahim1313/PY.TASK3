# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел
# Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
import math
a = int(input('введите количество элементов массива: '))
# arr = []
# for x in range(a):
#     rand = random.randrange(1, a+1, 1)
#     rand = random.randint(1, a)
#     arr.append(rand)
#     print(f"{rand}", end=' ')
# arr =  [random.randint(1, a) for x in range(1, a+1)]
# arr = random.randrange(1, a+1, 1)
arr = [x for x in range(1, a+1)]

for x in arr:
    print(f"{x}", end=' ')
    
print()
n = int(input('введите натуральное число: '))
diff = abs(n - arr[0])
number = arr[0]

for x in arr:
    if abs(n-x) < diff: 
        diff = abs(n-x)    
        number = x

print(f"{number}")