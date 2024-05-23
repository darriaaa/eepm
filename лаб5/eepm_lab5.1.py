import numpy as np

# Вхідні дані
# Матриця витрат
A = np.array([[600, 450],
              [450, 400]])

# Вектор попиту населення
d = np.array([1200, 700])

# Вектор доданої вартості (частки)
v = np.array([0.3, 0.5])

# Побудова матриці коефіцієнтів для рівняння
# (I - diag(v)) * X = d + A * e, де e - вектор одиниць
I = np.eye(2)
V = np.diag(v)
e = np.ones(2)

# Вектор сукупного попиту (включаючи проміжний та кінцевий попит)
b = d + A @ e

# Розв'язання системи лінійних рівнянь
X = np.linalg.solve(I - V, b)

# Вивід результатів
X_p, X_s = X
print(f"Ціна на продукцію промисловості: {X_p:.2f} млн. грн.")
print(f"Ціна на продукцію сільського господарства: {X_s:.2f} млн. грн.")
