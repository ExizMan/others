import math
import numpy as np


def erf(x, iter=100):
    result = 0.0
    for n in range(iter):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / (math.factorial(n) * (2 * n + 1))
        result += term

    return (2 / math.sqrt(math.pi)) * result


def determinant(matrix):
    # Проверка на квадратность матрицы
    if len(matrix) != len(matrix[0]):
        raise ValueError("Матрица должна быть квадратной")

    # Базовый случай: если матрица 2x2, вычисляем определитель напрямую
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0  # Инициализируем определитель

    for col in range(len(matrix)):
        # Вычисляем минор для каждой ячейки первой строки и рекурсивно вызываем функцию
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        sign = (-1) ** col  # Определяем знак

        # Рекурсивно добавляем результат в определитель
        det += sign * matrix[0][col] * determinant(minor)

    return det

def norm(row):
    x=0
    for i in range(len(row)):
        if row[i]!=0:
            x = 1/row[i]
            print([ t*x for t in row])
            return [ t*x for t in row]
def substr(row1,row2):
    rowres = []
    for i in range(len(row1)):
        rowres.append(row1[i] - row2[i])
    return rowres
def round_mant(row):
    print(row,"!")
    print([round(x,1) for x in row],'?')
    return [round(x,3) for x in row]

def matrix_rank(matrix):
    if not matrix:
        return 0

    num_rows = len(matrix)
    num_columns = len(matrix[0])
    rank = len(matrix)


    for i in range(num_rows-1):
        #print("!!",matrix[i])
        print("!!",matrix)
        matrix[i] = norm(matrix[i])
        matrix[i]=round_mant(matrix[i])
        print("??", matrix)
        for j in range(i+1,num_rows):
            matrix[j] = substr(norm(matrix[j]) , matrix[i])
            matrix[j] = round_mant(matrix[j])

    for row in matrix:
        is_exist = False
        for elem in row:
            if elem != 0:
                is_exist = True
        if not is_exist:
            rank -=1
    return rank


    '''
    for col in range(num_columns):
        found = False  # Флаг для поиска ненулевого элемента
        for row in range(rank, num_rows):
            if matrix[row][col] != 0:
                # Если найден ненулевой элемент в столбце, увеличиваем ранг и перемещаем строку с ненулевым элементом наверх
                matrix[rank], matrix[row] = matrix[row], matrix[rank]
                found = True
                break

        if found:
            # Обнуляем все элементы ниже найденного ненулевого элемента в столбце
            for i in range(rank + 1, num_rows):
                ratio = matrix[i][col] / matrix[rank][col]
                for j in range(col, num_columns):
                    matrix[i][j] -= ratio * matrix[rank][j]

            rank += 1

    return rank
    '''
A = [[1.00, 0.80, 0.64],
     [1.00, 0.90, 0.81],
     [1.00, 1.10, 1.21]]

# Вектор b с значениями функции ошибки erf
b = [erf(0.80), erf(0.90), erf(1.10)]



# Размерность матрицы A и вектора b
n = len(b)

# Прямой ход метода Гаусса
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

print("Решение x1, x2, x3:")
print(x)
print(f"erf(1.0) = {erf(1.0)}")
print(f"Сумма x1, x2, x3 = {np.sum(x)}\n")

# Матрица A
A = [[0.1, 0.2, 0.3],
     [0.4, 0.5, 0.6],
     [0.7, 0.8, 0.9]]

# Вектор b
b = [0.1, 0.3, 0.5]

n = len(A)

m = len(A[0])
# Расширенная матрица [A|b]

Ab = [row + [bi] for row, bi in zip(A, b)]



rank_A = matrix_rank(A)
# rank_Ab = matrix_rank(Ab)
# print(np.linalg.matrix_rank(A))
# print(np.linalg.matrix_rank(Ab))
print(rank_A)
# print(rank_Ab)
# # Проверка условия совместности
# if rank_A == rank_Ab and rank_A == m:
#     if (determinant(A) != 0):
#         print("Система совместна и имеет одно решение.")
#     else:
#         print("Система совместна и имеет множество решений.")
#
#
# else:
#     print("Система несовместна и не имеет решения.")
