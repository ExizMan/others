# Listing 4.15

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# Описание класса Perceptron
class Perceptron(object):

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta  # Темп обучения (от 0 до 1)
        self.n_iter = n_iter  # Количество итераций (уроков)

    '''
    Выполнить подгонку модели под тренировочные данные.
    Параметры
    X    - тренировочные данные: массив, размерность -  X[n_samples,
    n_features] , где 
                          n_samples - число образцов,
                          n_features - число признаков, 
    у - Целевые значения: массив, размерность - y[n_samples]
    Возвращает
    self: object
    '''
    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])  # w_: 1-мерный массив – Веса после обучения
        self.errors_ = []  # errors_: список – ошибок классификации в каждой эпохе
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
                self.errors_.append(errors)
        return self

     # Рассчитать чистый вход
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    # Вернуть метку класса после единичного скачка
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df = pd.read_csv(url, header=None)
print('Данные о цветках Ирис')
print(df.to_string())
df.to_csv('Iris.csv')

# Listing 4.17
# выборка из DF 100 строк (столбец 0 и столбец 2), загрузка их в массив X
X = df.iloc[0:100,[0, 2]].values
print('Значение X - 100')
print(X)

# выборка из DF 100 строк (столбец 4 название цветков) и загрузка
y = df.iloc[0:100,4].values

# Преобразование названий цветков (столбец 4) в массив чисел -1 и 1
y = np.where(y == 'Iris-setosa',-1, 1)
print('Значение названий цветков  в виде -1 и 1, Y - 100')
print(y)
print('-------')
ppn=Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_, marker='o')
plt.xlabel('Эпохи')
plt.xlabel('Ошибки')
plt.show()

