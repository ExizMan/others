from math import pow,pi
import time

nk = int(input("range: "))
for n in range(nk):
    start1 = time.perf_counter()
    row1 = 0
    for i in range(1, n + 1):
        row1 += 1 / (pow(i, 2) + 1)
    stop1 = time.perf_counter()


    row2 = 0
    start3 = time.perf_counter()
    for i in range(1, n + 1):

        row2 += 1 / (pow(i, 4) * (pow(i, 2) + 1))
    row2 = (pow(pi, 2) / 6) - (pow(pi, 4) / 90) + row2
    stop2 = time.perf_counter()
    print(f"range {n} ser1 {row1} time dif={stop1-start1}")
    print(f"range {n} ser2 {row2} time dif={stop2-start3}")
    print(f"dif {row2-row1}")