import matplotlib.pyplot as plt  # Імпорт бібліотеки для побудови графіків
import numpy as np  # Імпорт бібліотеки для роботи з масивами та математичними функціями

num_sectors = 7  # Визначаємо кількість секторів діаграми
values = np.random.randint(1, 100, size=num_sectors)  # Генеруємо випадкові значення для секторів у діапазоні від 1 до 100
labels = ['Sector 1', 'Sector 2', 'Sector 3', 'Sector 4', 'Sector 5', 'Sector 6', 'Sector 7']  # Підписи для секторів

fig, ax = plt.subplots()  # Створюємо фігуру та підграфік
explode = (0.2, 0.15, 0.18, 0.25, 0.1, 0, 0)  # Визначаємо, на скільки секторів "вибухнуть" (будуть відсунуто)

# Створюємо кругову діаграму з новими кольорами та стилем
ax.pie(values, labels=labels, autopct='%1.1f%%', explode=explode,
       colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ffcc00'])

plt.show()  # Відображаємо побудований графік
