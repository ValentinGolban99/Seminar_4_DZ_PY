# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def primfacs(n):
    i = 2
    primfac = []
    for i in range(1, n + 1):
        if(n % i == 0):
           primfac.append(i)
    return primfac

print(primfacs(int(input('Введите N: '))))

