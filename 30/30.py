"""Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

first_element=int(input("Введите первый элемент:"))
difference=int(input("Введите разность элементов:"))
number_of_elements=int(input("Введите количество элементов:"))
an=first_element+(number_of_elements-1)*difference
print(an)
for i in range (number_of_elements):
    print(first_element +i*difference, end="->")