import numpy as np

# Початкові умови
transition_rates = np.array([0.87] * 6 + [0.8])  # Коефіцієнти переходу
survival_rates = np.array([1] * 6 + [0.75])  # Коефіцієнти виживання
reproduction_vector = np.array([0, 0, 0.19, 0.44, 0.5, 0.5, 0.45])  # Вектор народжуваності

# Швидкість росту популяції
growth_rate = sum(transition_rates * survival_rates * reproduction_vector)

# Стійка вікова структура
stable_age_structure = (transition_rates * survival_rates) / sum(transition_rates * survival_rates)

# Величина H
lambda_l = sum(transition_rates * survival_rates)
H = (1 - (1 / lambda_l)) * 100

# Висновок
print("Швидкість росту популяції:", growth_rate)
print("Стійка вікова структура:", stable_age_structure)
print("Величина H:", H)
