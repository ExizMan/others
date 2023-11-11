from math import sqrt

def sign(x):
    if x>0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0



a,b,c = float(input("Введите a \n")), float(input("Введите b \n")), float(input("Введите c \n"))

d = b**2 - (4*a*c)
x1,x,x2 = 0,0,0
if d < 0:
    print("Корней нет")
elif d == 0:
    x = -b / (2*a)
    print(f"Корень {x}")
    x = -((b+sign(b)*sqrt(b**2 - (4*a*c)))/ (2*a))
    print(f"Корень через сигнум {x}")
else:
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b - sqrt(d)) / (2*a)
    print(f"Корни x1 = {x1}, x2 = {x2}")
    x1 = -((b+sign(b)*sqrt(b**2 - (4*a*c)))/ (2*a))
    x2 = c / (a*x1)
    print(f"Корни через сигнум x1 = {x1}, x2 = {x2}")



if b != 0:
    if d!=0:
        x1 = -2*c / (sign(b) * (abs(b) + sqrt(d)))
        x2 = -2*c / (sign(b) * (abs(b) - sqrt(d)))
