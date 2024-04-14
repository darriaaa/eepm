import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Функція, що представляє систему диференціальних рівнянь
def fish_population(x, t, r, q):
    dxdt = r * x * (1 - x / q) - p
    return dxdt

# Функція для обчислення p
def calculate_p(N, q):
    if 1 <= N <= 9:
        r = N / 2
    elif 10 <= N <= 18:
        r = N / 3
    else:
        r = N / 4
    p = r * q / 4
    return p

# Початкові значення
x0_1 = 0.3  # Перше початкове значення x
x0_2 = 0.7  # Друге початкове значення x

N = 2  # Кількість пар риби

# Обчислення значення q
if x0_1 < N / 2 < x0_2 or x0_2 < N / 2 < x0_1:
    q = N / 2
elif N / 3 < x0_1 < N / 2 < x0_2 or N / 3 < x0_2 < N / 2 < x0_1:
    q = N / 3
else:
    q = N / 4

# Обчислення значення p
p = calculate_p(N, q)

# Обчислення значення r
r = N / 2

# Час
t = np.linspace(0, 10, 100)

# Розв'язання системи диференціальних рівнянь для обох початкових значень
x1 = odeint(fish_population, x0_1, t, args=(r, q))
x2 = odeint(fish_population, x0_2, t, args=(r, q))

# Відображення результатів
plt.plot(t, x1, label='x0 = {}'.format(x0_1))
plt.plot(t, x2, label='x0 = {}'.format(x0_2))
plt.xlabel('Час')
plt.ylabel('Популяція риби')
plt.title('Динаміка популяції риби')
plt.legend()
plt.grid(True)
plt.show()
