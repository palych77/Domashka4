# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint
sp = list(map(int, input("Введите числа через пробел:\n").split()))
print(sp)
new = []
for i in sp:
    if i not in new:
        new.append(i)
print(new)