import numpy as np


# Размерность матрицы A и вектора b

A = [[10 ** -4, 1],
     [1, 2]]
b = [1, 4]

n = len(b)


# Прямой ход метода Гаусса
def gaus(A, b, n):
    for pivot in range(n):
        # Поиск максимального элемента в текущем столбце
        max_row = pivot
        for row in range(pivot + 1, n):
            if abs(A[row][pivot]) > abs(A[max_row][pivot]):
                max_row = row

        # Обмен строками
        A[pivot], A[max_row] = A[max_row], A[pivot]
        b[pivot], b[max_row] = b[max_row], b[pivot]

        # Приведение текущего столбца к единичному значению
        pivot_elem = A[pivot][pivot]
        for j in range(pivot, n):
            A[pivot][j] /= pivot_elem
        b[pivot] /= pivot_elem

        # Обнуление нижних элементов столбца
        for i in range(pivot + 1, n):
            factor = A[i][pivot]
            for j in range(pivot, n):
                A[i][j] -= factor * A[pivot][j]
            b[i] -= factor * b[pivot]

    # Обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
    return x


# Вызов функции gaus для решения системы
x = gaus(A, b, n)

# Невязки
residuals = [b[i] - sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]

# Вывод решения и невязок
print("Решение 1:")
for i in range(n):
    print(f"x[{i}] = {x[i]}")

print("\nНевязки:")
for i in range(n):
    print(f"Невязка {i}: {residuals[i]}")

residuals = np.dot(A, x) - b

# Вывод невязок
print("\nНевязки с numpy:")
for i in range(n):
    print(f"Невязка {i}: {residuals[i]}")

print("\n")
A = [[2.34, -4.21, -11.61],
     [8.04, 5.22, 0.27],
     [3.92, -7.99, 8.37]]
b = [14.41, -6.44, 55.56]

n = len(b)

x = gaus(A, b, n)

# Невязки
residuals = [b[i] - sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]

# Вывод решения и невязок
print("Решение 2:")
for i in range(n):
    print(f"x[{i}] = {x[i]}")

print("\nНевязки:")
for i in range(n):
    print(f"Невязка {i}: {residuals[i]}")

residuals = np.dot(A, x) - b

# Вывод невязок
print("\nНевязки с numpy:")
for i in range(n):
    print(f"Невязка {i}: {residuals[i]}")
print("\n")



A = [[4.43, -7.21, 8.05, 1.23, -2.56],
     [-1.29, 6.47, 2.96, 3.22, 6.12],
     [6.12, 8.31, 9.41, 1.78, -2.88],
     [-2.57, 6.93, -3.74, 7.41, 5.55],
     [1.46, 3.62, 7.83, 6.25, -2.35]]

b = [2.62, -3.97, -9.12, 8.11, 7.23]

n = len(b)

x = gaus(A, b, n)

# Невязки
residuals = [b[i] - sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]

# Вывод решения и невязок
print("Решение 3:")
for i in range(n):
    print(f"x[{i}] = {x[i]}")

print("\nНевязки:")
for i in range(n):
    print(f"Невязка {i}: {residuals[i]}")

residuals = np.dot(A, x) - b

# Вывод невязок
print("\nНевязки с numpy:")
for i in range(n):
    print(f"Невязка {i}: {residuals[i]}")
