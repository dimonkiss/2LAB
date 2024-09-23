import numpy as np
import matplotlib.pyplot as plt
def plot_functions():
    # Створюємо x в діапазоні від -10 до 10
    x = np.linspace(-10, 10, 400)

    # Визначаємо функції
    f_x = x ** 2 - 1
    g_x = np.sin(x)

    # Створюємо subplot з 1 рядком і 2 стовпцями
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Перше поле: графік f(x) = x^2 - 1 (синій графік)
    ax1.plot(x, f_x, color='blue')
    ax1.set_title('Графік f(x) = x^2 - 1')
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.grid(True)

    # Друге поле: графік g(x) = sin(x) (червоний графік)
    ax2.plot(x, g_x, color='red')
    ax2.set_title('Графік g(x) = sin(x)')
    ax2.set_xlabel('x')
    ax2.set_ylabel('g(x)')
    ax2.grid(True)

    # Показуємо графіки
    plt.tight_layout()  # Щоб графіки не накладались
    plt.show()


def plot_functions_with_intersection():
    # Створюємо x в діапазоні від -10 до 10
    x = np.linspace(-10, 10, 400)

    # Визначаємо функції
    f_x = x ** 2 - 1
    g_x = np.sin(x)

    # Створюємо графік
    fig, ax = plt.subplots(figsize=(8, 6))

    # Побудова графіку f(x) = x^2 - 1 (синій, товщина лінії 2)
    ax.plot(x, f_x, color='blue', label=r'$f(x) = x^2 - 1$', linewidth=2)

    # Побудова графіку g(x) = sin(x) (червоний, товщина лінії 1.5)
    ax.plot(x, g_x, color='red', label=r'$g(x) = \sin(x)$', linewidth=1.5)

    # Виділення осей координат
    ax.axhline(0, color='black', linewidth=1)  # Вісь x
    ax.axvline(0, color='black', linewidth=1)  # Вісь y

    # Знаходимо точки перетину функцій (наближено)
    intersection_indices = np.isclose(f_x, g_x, atol=0.1)  # Шукаємо точки, де різниця функцій менша за 0.1
    intersection_x = x[intersection_indices]
    intersection_y = f_x[intersection_indices]

    # Відображаємо точки перетину
    ax.scatter(intersection_x, intersection_y, color='green', zorder=5, label='Точки перетину')

    # Підписуємо осі
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Додаємо заголовок
    plt.title("Графіки функцій $f(x) = x^2 - 1$ та $g(x) = \sin(x)$")

    # Підписуємо графіки всередині вікна
    ax.text(-9, 50, r'$f(x) = x^2 - 1$', color='blue', fontsize=12)
    ax.text(6, 0.5, r'$g(x) = \sin(x)$', color='red', fontsize=12)

    # Додаємо сітку
    ax.grid(True)

    # Додаємо легенду
    ax.legend()

    # Відображаємо графік
    plt.show()

# Виклик функції
plot_functions()

# Виклик функції
plot_functions_with_intersection()