# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
min= int (input ('Введите минимум '))
max= int (input ('Введите максимум '))
a=[randint (1,19) for i in range (10)]
print (*a)
list1=[]
for i in range(len(a)):
    if a[i]>min and a[i]<max:
        list1.append(i)
print (*list1)