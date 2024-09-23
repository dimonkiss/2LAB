import numpy as np
import matplotlib.pyplot as plt
def plot_polar_curve():
    # Параметр α (кут в радіанах) від 0 до 2π
    alpha = np.linspace(0, 2 * np.pi, 500)

    # Визначаємо p(α) згідно з формулою
    p = 0.5 / (1 + 0.5 * np.cos(alpha))

    # Створюємо графік в полярній системі координат
    plt.polar(alpha, p, label=r'$p = \frac{0.5}{1+0.5\cdot \cos(\alpha)}$', color='green')

    # Підписуємо заголовок
    plt.title('Крива другого порядку в полярних координатах')

    # Додаємо легенду
    plt.legend()

    # Відображаємо графік
    plt.show()

# Виклик функції
plot_polar_curve()