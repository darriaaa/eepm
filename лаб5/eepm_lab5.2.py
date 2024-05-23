import math

# Допоміжні функції для роботи з матрицями

def matmul(A, B):
    """ Множення двох матриць """
    result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result

def matadd(A, B):
    """ Додавання двох матриць """
    result = [[a + b for a, b in zip(A_row, B_row)] for A_row, B_row in zip(A, B)]
    return result

def transpose(A):
    """ Транспонування матриці """
    return [list(row) for row in zip(*A)]

def identity_matrix(size):
    """ Створення одиничної матриці заданого розміру """
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def matdiff(A, B):
    """ Різниця двох матриць """
    return [[a - b for a, b in zip(A_row, B_row)] for A_row, B_row in zip(A, B)]

def inverse_matrix(A):
    """ Знаходження оберненої матриці за допомогою розширеної матриці """
    size = len(A)
    I = identity_matrix(size)
    AI = [A_row + I_row for A_row, I_row in zip(A, I)]
    
    # Прямий хід методу Гаусса
    for i in range(size):
        # Поділ рядка, щоб головний елемент був 1
        factor = AI[i][i]
        AI[i] = [x / factor for x in AI[i]]
        
        # Зведення нижніх рядків до нуля
        for j in range(i+1, size):
            factor = AI[j][i]
            AI[j] = [x - factor * y for x, y in zip(AI[j], AI[i])]
    
    # Зворотний хід методу Гаусса
    for i in range(size-1, -1, -1):
        for j in range(i-1, -1, -1):
            factor = AI[j][i]
            AI[j] = [x - factor * y for x, y in zip(AI[j], AI[i])]
    
    # Вилучення оберненої матриці з розширеної матриці
    inverse = [row[size:] for row in AI]
    return inverse

def eigen_decomposition_3x3(A):
    """ Знаходження власних чисел та власних векторів для 3x3 матриці """
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]
    
    # Знаходження коефіцієнтів характеристичного поліному
    p1 = -(a + e + i)
    p2 = (a*e + e*i + i*a - c*g - b*f - d*h)
    p3 = -(a*e*i + b*f*g + c*d*h - a*f*h - b*d*i - c*e*g)
    
    # Знаходження власних чисел (коренів кубічного рівняння)
    Q = (3*p2 - p1**2) / 9
    R = (9*p1*p2 - 27*p3 - 2*p1**3) / 54
    D = Q**3 + R**2  # Дискримінант

    if D >= 0:
        # Одне дійсне коріння
        S = math.copysign(abs(R + math.sqrt(D))**(1/3), R + math.sqrt(D))
        T = math.copysign(abs(R - math.sqrt(D))**(1/3), R - math.sqrt(D))
        eig1 = -p1 / 3 + (S + T)
        eig2 = -p1 / 3 - (S + T) / 2
        eig3 = -p1 / 3 - (S + T) / 2
    else:
        # Три дійсних корені
        th = math.acos(R / (-Q**3)**0.5)
        eig1 = 2 * (-Q)**0.5 * math.cos(th / 3) - p1 / 3
        eig2 = 2 * (-Q)**0.5 * math.cos((th + 2*math.pi) / 3) - p1 / 3
        eig3 = 2 * (-Q)**0.5 * math.cos((th + 4*math.pi) / 3) - p1 / 3

    eigenvalues = [eig1, eig2, eig3]

    def eigenvector_for_eigenvalue(A, eigenvalue):
        I = identity_matrix(len(A))
        AI = matdiff(A, [[eigenvalue if i == j else 0 for j in range(len(A))] for i in range(len(A))])
        
        # Прямий хід методу Гаусса для знаходження власного вектора
        for i in range(len(A)):
            factor = AI[i][i]
            if factor == 0:
                continue
            AI[i] = [x / factor for x in AI[i]]
            for j in range(i+1, len(A)):
                factor = AI[j][i]
                AI[j] = [x - factor * y for x, y in zip(AI[j], AI[i])]

        # Зворотний хід методу Гаусса
        for i in range(len(A)-1, -1, -1):
            for j in range(i-1, -1, -1):
                factor = AI[j][i]
                AI[j] = [x - factor * y for x, y in zip(AI[j], AI[i])]
        
        # Вибір власного вектора
        eigenvector = [0] * len(A)
        for i in range(len(A)):
            eigenvector[i] = 1 if AI[i][i] == 1 else 0

        return eigenvector

    eigenvectors = [eigenvector_for_eigenvalue(A, eig) for eig in eigenvalues]

    return eigenvalues, eigenvectors

# Вхідні дані
A = [[0.5, 0.1, 0.5],
     [0, 0.3, 0.1],
     [0.2, 0.3, 0.1]]

# 1. Власні числа та власні вектори
eigenvalues, eigenvectors = eigen_decomposition_3x3(A)
print("Власні числа матриці A:")
for i, val in enumerate(eigenvalues):
    print(f"{i+1}: {val:.4f}")

print("Власні вектори матриці A:")
for i, vec in enumerate(eigenvectors):
    print(f"{i+1}: {vec}")

# 2. Характеристичний поліном
a, b, c = A[0]
d, e, f = A[1]
g, h, i = A[2]

# Знаходження коефіцієнтів характеристичного поліному
p1 = -(a + e + i)
p2 = (a*e + e*i + i*a - c*g - b*f - d*h)
p3 = -(a*e*i + b*f*g + c*d*h - a*f*h - b*d*i - c*e*g)

coeffs = [1, p1, p2, p3]
print("Коефіцієнти характеристичного поліному:", coeffs)

# 3. Число Фробеніуса
frobenius_number = max(abs(val) for val in eigenvalues)
print("Число Фробеніуса:", frobenius_number)

# 4. Правий та лівий вектори Фробеніуса
index = eigenvalues.index(frobenius_number)
right_frobenius_vector = eigenvectors[index]
right_frobenius_vector = [x / sum(right_frobenius_vector) for x in right_frobenius_vector]

left_eigenvalues, left_eigenvectors = eigen_decomposition_3x3(transpose(A))
left_frobenius_vector = left_eigenvectors[index]
left_frobenius_vector = [x / sum(left_frobenius_vector) for x in left_frobenius_vector]

print("Правий вектор Фробеніуса:", right_frobenius_vector)
print("Лівий вектор Фробеніуса:", left_frobenius_vector)

# 5. Висновок про продуктивність
is_productive = all(x > 0 for x in right_frobenius_vector) and all(x > 0 for x in left_frobenius_vector)
print("Матриця продуктивна" if is_productive else "Матриця не продуктивна")

# 6. Матриця повних витрат
I = identity_matrix(len(A))
B = inverse_matrix(matdiff(I, A))
print("Матриця повних витрат B:\n", B)

# 7. Дослідження на збіжність ряду
tolerance = 0.01
max_iter = 1000

current_sum = identity_matrix(len(A))
previous_sum = [[0]*len(A) for _ in range(len(A))]
A_power = [row[:] for row in A]

for i in range(1, max_iter):
    current_sum = matadd(current_sum, A_power)
    if all(all(abs(current_sum[i][j] - previous_sum[i][j]) < tolerance for j in range(len(A))) for i in range(len(A))):
        print(f"Сума ряду збігається на ітерації {i}")
        break
    previous_sum = [row[:] for row in current_sum]
    A_power = matmul(A_power, A)

print("Матриця повних витрат (підрахована через ряд):\n", current_sum)

# 8. Знаходження вектора цін
s = [0.2, 0.3, 0.4]
p = matmul(transpose(B), [[x] for x in s])
p = [x[0] for x in p]
print("Вектор цін:", p)
