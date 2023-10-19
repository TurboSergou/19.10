"""
Задание 2
Создайте класс для подсчета максимума из четырех аргументов,
минимума из четырех аргументов,
средне-арифметического из четырех аргументов,
факториала аргумента.
Функциональность необходимо реализовать в виде статических методов.
"""
import math

class Schet():

    @staticmethod
    def max(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def min(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def avg(a, b, c, d):
        return (a + b + c + d) / 4
    @staticmethod
    def fact(n):
        if n==0 or n==1:
            return 1
        else:
            p = 1
            for i in range(1, n+1):
                p *= i
            return p


print(Schet.max(1,3,4,7))
print(Schet.min(1,3,4,7))
print(Schet.avg(1,3,4,7))
print(Schet.fact(5))
