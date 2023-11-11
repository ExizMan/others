import random
from c1 import C1
from c2 import C2
from c3 import C3

shapes = []
for _ in range(15):
    choice = random.randint(1, 3)
    if choice == 1:
        shapes.append(C1(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))
    elif choice == 2:
        shapes.append(C2(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))
    else:
        shapes.append(C3(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))

# Выводим информацию о фигурах
for i, shape in enumerate(shapes):
    print(f"Фигура {i+1}:")
    print(f"Площадь: {shape.square()}")
    print(f"Периметр: {shape.perimeter()}")
    shape.fill(f"Color{i+1}")
    print(f"Цвет заливки: {shape.color}")

# Сравниваем фигуры по площади, определяем пересечения и включения
for i in range(len(shapes)):
    for j in range(i + 1, len(shapes)):
        if shapes[i].compare(shapes[j]):
            print(f"Фигура {i+1} и фигура {j+1} имеют одинаковую площадь")
        if shapes[i].is_intersect(shapes[j]):
            print(f"Фигура {i+1} и фигура {j+1} пересекаются")
        if shapes[i].is_include(shapes[j]):
            print(f"Фигура {j+1} включена в фигуру {i+1}")