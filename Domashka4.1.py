# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math

n=int(input("Введите число: "))
sp = []
for i in range(2, int(math.sqrt(n)) + 1): # обычно делитель не будет больше корня
    while (n % i == 0): # while, а не if
        sp.append(i)
        n //= i # убираем множитель из числа
print(sp)
if (n != 1): # но один делитель может быть больше корня
    print (n)