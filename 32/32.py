"""Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)"""
import random
print (list1:=[random.randint(1,20) for i in range(10)])
list2=[]
max=12
min=3
for i in range(len(list1)):
    if list1[i]>=min and list1[i]<=max:
        list2.append(i)
print(list2)     

