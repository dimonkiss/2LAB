import numpy as np
import matplotlib.pyplot as plt

def plot_parametric_curve():
    # Параметр t в діапазоні від -10 до 10
    t = np.linspace(-10, 10, 500)

    # Визначення x(t) та y(t) згідно з заданими рівняннями
    x = t**2 / (1 + t**2)
    y = t / (1 + t**2)

    # Створення графіка
    plt.plot(x, y, label=r'$y = \frac{t}{1+t^2}$, $x = \frac{t^2}{1+t^2}$', color='blue')

    # Підписуємо осі
    plt.xlabel('x(t)')
    plt.ylabel('y(t)')

    # Додаємо заголовок
    plt.title('Параметрично задана крива')

    # Додаємо легенду
    plt.legend()

    # Відображаємо графік
    plt.grid(True)
    plt.show()

# Виклик функції
plot_parametric_curve()