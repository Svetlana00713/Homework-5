# Задача 28: Напишите рекурсивную функцию sum(a,b), возвращающую
# сумму двух целых неотрицательных чисел. Из всех арифметических
# операций допускаются только +1 и -1. Также нельзя использовать
# циклы.

a = int(input("Введите натуральное число a: "))
b = int(input("Введите натуральное число b: "))
def sum(a, b):
    if a == 0:
        return b;
    return sum(a-1, b+1)
print("Сумма чисел равна", sum(a, b))
