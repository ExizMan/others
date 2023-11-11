import math
import time

xlist = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.999999999]
s1, s2, s = 0, 0, 0
k = int(input("Введите кол-во операций: "))

start = time.perf_counter()
for i in range(0, len(xlist), 1):
    for j in range(1, k, 1):
        s1 += 1 / (math.sqrt(math.pow(k, 3) + xlist[i]))
        s2 += 1 / (math.sqrt(math.pow(k, 3) - xlist[i]))
    s = s1 - s2
    print("Для Х = " + str(xlist[i]) + " и кол-ва операций " + str(k) + " результат: " + str(s))
    s1, s2, s = 0, 0, 0
finish = time.perf_counter()
print("Время подсчёта обоих рядов для кол-ва операций " + str(k) + f" равно {finish - start:0.4f}")