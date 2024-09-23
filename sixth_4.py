import matplotlib.pyplot as plt  # Імпорт бібліотеки для побудови графіків
import numpy as np  # Імпорт бібліотеки для роботи з масивами та математичними функціями

num_dots = 21  # Визначаємо кількість точок для розсіювання
# Генеруємо випадкові значення для координат x та y у діапазоні від 50 до 100
values_x = np.random.randint(50, 100, size=num_dots)
values_y = np.random.randint(50, 100, size=num_dots)

# Визначаємо можливі маркери та кольори для точок
markers = ['x', '*', '^', '>', '<', 'v']
colors = ['red', 'blue', 'green', 'orange', 'purple']

# Цикл для побудови кожної точки з відповідними кольором та маркером
for i in range(num_dots):
    plt.scatter(values_x[i], values_y[i],
                c=colors[i % len(colors)],  # Вибір кольору за модулем
                marker=markers[i % len(markers)])  # Вибір маркера за модулем

plt.xlabel('X координата')  # Підписуємо вісь x
plt.ylabel('Y координата')  # Підписуємо вісь y
plt.title('Графік розсіювання з різними кольорами і маркерами')  # Заголовок графіка
plt.grid(True)  # Додаємо сітку для покращення читабельності
plt.show()  # Відображаємо побудований графік
