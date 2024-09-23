import numpy as np
import matplotlib.pyplot as plt


def plot_quadratic_curve():
    # Створюємо координати x та y
    x = np.linspace(-3, 3, 400)
    y = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x, y)

    # Визначаємо функцію для кривої
    Z = 40 * X ** 2 + 36 * X * Y + 25 * Y ** 2 - 8 * X - 14 * Y + 1

    # Створюємо графік
    plt.contour(X, Y, Z, levels=[0], colors='blue')

    # Підписуємо графік ближче до кривої під кутом α = 12°
    angle = 12
    plt.text(0.5, 0.5, 'Крива другого порядку', fontsize=12, rotation=angle, ha='center')

    # Підписуємо осі
    plt.xlabel('x')
    plt.ylabel('y')

    # Додаємо заголовок
    plt.title('Крива другого порядку')

    # Встановлюємо однакові масштаби для осей
    plt.axis('equal')
    plt.grid(True)

    # Відображаємо графік
    plt.show()


# Виклик функції
plot_quadratic_curve()
