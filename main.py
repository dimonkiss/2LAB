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


def plot_curve(alpha_deg):
    # Кут повороту в радіанах
    alpha_rad = np.radians(alpha_deg)

    # Створюємо сітку координат для x і y
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)

    # Обчислюємо поворот координат
    X_rot = X * np.cos(alpha_rad) + Y * np.sin(alpha_rad)
    Y_rot = -X * np.sin(alpha_rad) + Y * np.cos(alpha_rad)

    # Задаємо рівняння 40x^2 + 36xy + 25y^2 - 8x - 14y + 1 = 0
    Z = (40 * X_rot ** 2 + 36 * X_rot * Y_rot + 25 * Y_rot ** 2
         - 8 * X_rot - 14 * Y_rot + 1)

    # Створюємо графік рівняння
    plt.contour(X, Y, Z, levels=[0], colors='red')

    # Додаємо заголовок і підпис кута
    plt.title(f'Крива другого порядку з поворотом на α = {alpha_deg}°')

    # Відображаємо графік
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


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

# Виклик функції
plot_parametric_curve()

# Виклик функції
plot_polar_curve()

# Виклик функції з α = 12°
plot_curve(12)

# Виклик функції
plot_functions()

# Виклик функції
plot_functions_with_intersection()

# Виклик функцій для побудови графіків
plot_two_graphs_together()    # Графіки на одній площині
plot_two_graphs_in_subplots() # Графіки в різних полях