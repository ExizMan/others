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
        return np.dot(X, self.w_[1:])+self.w_[0]

    # Вернуть метку класса после единичного скачка
    def predict(self, X):
        print(self.w_)
        return np.where(self.net_input(X) >= 0.0, 1, -1)


class AdaptiveLinearNeuron(object):
    '''
    Классификатор на основе ADALINE (ADAptive Linear NEuron).
    Параметры
    eta : float - Темп обучения (между 0.0 и 1.0)
    n iter : in - Проходы по тренировочному набору данных
    Атрибуты
    w_ : 1-мерный массив - Веса после подгонки.
    errors_ : список - Число случаев ошибочной классификации в каждой эпохе.
    '''
    def __init__(self, rate=0.01, niter=10):
         self.rate = rate
         self.niter = niter

    def fit(self, X, y):
        ''' Выполнить подгонку под тренировочные данные.
        Параметры
        X : (массив}, форма = [n_samples, n_features] -Тренировочные векторы,
                           где n_samples - число образцов
                              n_features - число признаков.
        у : массив, форма = [n_samples] - Целевые значения.
        Возвращает
        self : объект
        '''

        self.weight = np.zeros(1 + X.shape[1])
        self.cost = []
        for i in range(self.niter):
            output = self.net_input(X)
            print('123-456')
            errors = y - output
            print(self.rate * X.T.dot(errors))
            print('666-111')
            self.weight[1:] += self.rate * X.T.dot(errors)
            self.weight[0] += self.rate * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost.append(cost)
        return self


    def net_input(self, X):
        # Calculate net input"""
        print('1------')
        print(np.dot(X, self.weight[1:]) + self.weight[0])
        print('2------')
        return np.dot(X, self.weight[1:]) + self.weight[0]

    def activation(self, X):
        # Compute linear activation"""
       return self.net_input(X)

    def predict(self, X):
        print(self.weight)
        return np.where(self.activation(X) >= 0.0, 1, -1)



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
ppn=AdaptiveLinearNeuron(rate=0.1, niter=10)
ppn.fit(X, y)
i1=[5.5, 1.6]
i2=[6.4, 4.5]
i3=[5.9, 2.0]
print(ppn.predict(i1))
print(ppn.predict(i2))
print(ppn.predict(i3))

'''plt.scatter(X[0:50, 0], X[0:50, 1], color='red', marker='o', label='щетинистый')
# Следующие 50 элементов (Строки 50-100, столбцы 0,1)
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='разноцветный')

# Формировние названий осей и вывод графика на экран
plt.xlabel('длина чашелистика')
plt.ylabel('длина лепестка')
plt.legend(loc='upper left')
plt.show()'''

