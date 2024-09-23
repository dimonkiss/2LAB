import numpy as np
import matplotlib.pyplot as plt

def plot_two_graphs_together():
    # Створюємо значення для x і y
    x = np.linspace(-10, 10, 400)
    y_parabola = np.sqrt(16 * x)  # Для y^2 = 16x (позитивна гілка параболи)
    y_parabola_neg = -np.sqrt(16 * x)  # Для y^2 = 16x (негативна гілка параболи)

    # Для лінії x + y - 4 = 0 (y = 4 - x)
    y_line = 4 - x

    # Створюємо графік
    plt.figure(figsize=(8, 6))

    # Побудова параболи
    plt.plot(x, y_parabola, color='blue', label=r'$y^2 = 16x$', linewidth=2)
    plt.plot(x, y_parabola_neg, color='blue', linewidth=2)  # Негативна гілка

    # Побудова лінії
    plt.plot(x, y_line, color='red', label=r'$x + y - 4 = 0$', linestyle='--', linewidth=2)

    # Підписуємо осі
    plt.xlabel('x')
    plt.ylabel('y')

    # Додаємо заголовок
    plt.title('Два графіки на одній площині')

    # Додаємо легенду
    plt.legend()

    # Відображаємо сітку
    plt.grid(True)

    # Відображаємо графік
    plt.show()


def plot_two_graphs_in_subplots():
    # Створюємо значення для x і y
    x = np.linspace(-10, 10, 400)
    y_parabola = np.sqrt(16 * x)  # Для y^2 = 16x (позитивна гілка параболи)
    y_parabola_neg = -np.sqrt(16 * x)  # Для y^2 = 16x (негативна гілка параболи)

    # Для лінії x + y - 4 = 0 (y = 4 - x)
    y_line = 4 - x

    # Створюємо subplot з 1 рядком і 2 стовпцями
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Перше поле: парабола
    ax1.plot(x, y_parabola, color='green', label=r'$y^2 = 16x$', linewidth=2)
    ax1.plot(x, y_parabola_neg, color='green', linewidth=2)  # Негативна гілка
    ax1.set_title(r'$y^2 = 16x$')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid(True)
    ax1.legend()

    # Друге поле: лінія
    ax2.plot(x, y_line, color='purple', label=r'$x + y - 4 = 0$', linestyle='-.', linewidth=2)
    ax2.set_title(r'$x + y - 4 = 0$')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.grid(True)
    ax2.legend()

    # Відображаємо графіки
    plt.tight_layout()
    plt.show()









# Виклик функцій для побудови графіків
plot_two_graphs_together()    # Графіки на одній площині
plot_two_graphs_in_subplots() # Графіки в різних полях