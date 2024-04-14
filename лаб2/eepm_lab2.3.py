import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Функція, що представляє систему диференціальних рівнянь
def fish_population(x, t, r, q, p):
    dxdt = r * x * (1 - x / q) - p
    return dxdt

# Параметри
N = 2  # Кількість пар риби

# Визначення значень r та q згідно з умовами
if 1 <= N <= 9:
    r = N / 2
    q = N / 2
elif 10 <= N <= 18:
    r = N / 3
    q = N / 3
else:
    r = N / 4
    q = N / 4

# Обчислення параметра p
a = 0.2  # Параметр a
p = r * q / 4 + a**2

# Початкове значення
x0 = 1  # Наприклад, можемо обрати будь-яке значення

# Час
t = np.linspace(0, 10, 100)

# Розв'язання системи диференціальних рівнянь
x = odeint(fish_population, x0, t, args=(r, q, p))

# Відображення результатів
plt.plot(t, x)
plt.xlabel('Час')
plt.ylabel('Популяція риби')
plt.title('Динаміка популяції риби')
plt.grid(True)
plt.show()
