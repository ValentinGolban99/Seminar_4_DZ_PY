# Вычислить число пи с заданной точностью d.

# формула Лейбница
# x = 4 - 4/3 + 4/5 - 4/7 + 4/9 - ... и т.д

k = 1
s = 0
for i in range (1000000):
    if i % 2 == 0:
        s += 4 / k
    else :
        s -= 4 / k
    k += 2
print(s)




