from math import sqrt, pow


def findseriasone(x: float, rng: float):
    ser1 = 0
    for i in range(1, rng,1):
        ser1 += 1 /( sqrt((pow(rng, 3)) + x))
    return ser1


def findseriastwo(x: float, rng: float):
    ser2 = 0
    for i in range(1, rng,1):
        ser2 += 1 /( sqrt((pow(rng, 3)) - x))
    return ser2


n = int(input('range'))
xk = [round(0.1*i, 1) for i in range(10)]
xk.append(0.999999999)
print(xk)
for x in xk:
    for i in range(1, n - 1):
        print(findseriasone(x, i + 1) - findseriasone(x, i))
    print("sled ser")
    for i in range(1, n - 1):
        print(findseriastwo(x, i + 1) - findseriastwo(x, i))
    print("----")
for x in xk:
    print(findseriasone(x, n)- findseriastwo(x, n))
