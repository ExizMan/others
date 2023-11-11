# Listing 4.16
# Загрузка из интернета данных, запись их в объект DataFrame  и вывод на печать
import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df = pd.read_csv(url, header=None)
print('Данные о цветках Ирис')
print(df.to_string())
df.to_csv('Iris.csv')
