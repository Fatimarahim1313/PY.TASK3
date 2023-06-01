# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

a = int(input('введите количество элементов массива: '))
# arr = []
# for x in range(a):
#     rand = random.randint(1, 10)
#     arr.append(rand)
#     print(f"{rand}", end=' ')

arr = [x for x in range(1, a+1)]
#arr = [random.randint(1, 10) for x in range(1, 11)]
for x in arr:
    print(f"{x}", end=' ')
print()
n = int(input('введите число для поиска: '))

print(arr.count(n))