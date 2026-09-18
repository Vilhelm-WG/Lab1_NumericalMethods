import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fixed_point, newton

#  Рівняння 1: Алгебраїчне (для методу Ньютона)
def f1(x):
    return x**4 + 4 * x**3 + 4.8 * x**2 + 16 * x + 1

def df1(x):
    return 4 * x**3 + 12 * x**2 + 9.6 * x + 16

#  Рівняння 2: Трансцендентне метод простої ітерації
def f2(x):
    return np.exp(x) - np.exp(-x) - 2

# Функція ітерації: x = phi(x) => x = ln(2 + e^{-x})
def phi2(x):
    return np.log(2 + np.exp(-x))


#  реалізація: Метод Ньютона дотичних
def newton_method_custom(f, df, x0, tol=1e-3, max_iter=100):
    x = x0
    residuals = []
    for i in range(max_iter):
        fx = f(x)
        residuals.append(abs(fx))
        if abs(fx) < tol:
            break
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Похідна дорівнює нулю.")
        x_next = x - fx / dfx
        if abs(x_next - x) < tol:
            break
        x = x_next
    return x, residuals


# реалізація: Метод простої ітерації
def simple_iteration_custom(phi, x0, tol=1e-3, max_iter=100):
    x = x0
    residuals = []
    for i in range(max_iter):
        x_next = phi(x)
        res = abs(x_next - x)
        residuals.append(res)
        if res < tol:
            break
        x = x_next
    return x, residuals


if __name__ == "__main__":
    x0_newton = -0.1
    x0_iter = 0.5

    #  Метод Ньютона
    root_newton_custom, res_newton_custom = newton_method_custom(f1, df1, x0=x0_newton)
    root_newton_scipy = newton(f1, x0=x0_newton, fprime=df1, tol=1e-3, disp=False)

    #  Метод простої ітерації
    root_iter_custom, res_iter_custom = simple_iteration_custom(phi2, x0=x0_iter)
    root_iter_scipy = fixed_point(phi2, x0=x0_iter, xtol=1e-3)

    print(f"Корінь (Метод Ньютона власна): {root_newton_custom:.4f}")
    print(f"Корінь (Метод Ньютона SciPy): {root_newton_scipy:.4f}")
    print(f"Корінь (Проста ітерація власна): {root_iter_custom:.4f}")
    print(f"Корінь (Проста ітерація SciPy): {root_iter_scipy:.4f}")

    plt.figure(figsize=(10, 6))

    plt.plot(range(len(res_newton_custom)), res_newton_custom, 'o-', label='Метод Ньютона (нев\'язка |f(x)|)', color='blue')
    plt.plot(range(len(res_iter_custom)), res_iter_custom, 's-', label='Метод простої ітерації (|x_{k+1} - x_k|)', color='orange')

    plt.yscale('log')
    plt.xlabel('Номер ітерації (k)', fontsize=12)
    plt.ylabel('Нев\'язка (логарифмічна шкала)', fontsize=12)
    plt.title('Порівняння швидкості збіжності методів', fontsize=14)
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.show()