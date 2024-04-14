import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Функція, що представляє систему диференціальних рівнянь
def fish_population(x, t, r, q, p):
    dxdt = r * x * (1 - x / q) - p
    return dxdt

# Функція для обчислення p
def calculate_p(r, q, a):
    return r * q / 4 - a**2

# Функція для обчислення r та q згідно з умовами
def calculate_r_q(N):
    if 1 <= N <= 9:
        r = N / 2
        q = N / 2
    elif 10 <= N <= 18:
        r = N / 3
        q = N / 3
    else:
        r = N / 4
        q = N / 4
    return r, q

# Початкові значення
N = 2  # Кількість пар риби
x0_1 = 0.1  # Перше початкове значення x, x₀ < x₁
x0_2 = 1.5  # Друге початкове значення x, x₂ > x₀ > x₁
x0_3 = 0.8  # Третє початкове значення x, x₂ < x₀ < q

# Обчислення параметрів r та q
r, q = calculate_r_q(N)

# Обчислення параметра p
a = 1  # Параметр a
p = calculate_p(r, q, a)

# Час
t = np.linspace(0, 10, 100)

# Розв'язання системи диференціальних рівнянь для кожного початкового значення
x1 = odeint(fish_population, x0_1, t, args=(r, q, p))
x2 = odeint(fish_population, x0_2, t, args=(r, q, p))
x3 = odeint(fish_population, x0_3, t, args=(r, q, p))

# Відображення результатів
plt.plot(t, x1, label='x0 = {}'.format(x0_1))
plt.plot(t, x2, label='x0 = {}'.format(x0_2))
plt.plot(t, x3, label='x0 = {}'.format(x0_3))
plt.xlabel('Час')
plt.ylabel('Популяція риби')
plt.title('Динаміка популяції риби')
plt.legend()
plt.grid(True)
plt.show()
