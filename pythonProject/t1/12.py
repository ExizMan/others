from collections import  Counter

fname = input("Введите имя файла: ")

file_opened =False
while file_opened == False:
    # Попытка открыть файл
    try:
        inf = open(fname, "r")
        file_opened = True
    except FileNotFoundError:
        # Показываем сообщение и запрашиваем имя файла повторно
        print("Файл не найден. Попробуйте еще.")
        fname = input("Введите имя файла: ")

a = inf.read().split()
print(a[0:10])
for i in range(len(a)):
    a[i]=a[i].strip(r"/'.[]{}()123456789")
    a[i] = a[i].lower()
print(a[0:10])
print(Counter(a).most_common(10))
=