import numpy as np
import matplotlib.pyplot as plt

# Дані про ціни, попит та пропозицію
prices = np.array([1.1, 1.3, 2.45, 2.7, 3.8, 5.2, 6.25])
demand = np.array([100, 85, 55, 45, 31, 18, 17])
supply = np.array([15, 30, 50, 55, 70, 95, 105])

# Знах аналітичний вигляд функцій попиту та пропозиції
demand_coefficients = np.polyfit(prices, demand, 1)
supply_coefficients = np.polyfit(prices, supply, 1)

demand_function = np.poly1d(demand_coefficients)
supply_function = np.poly1d(supply_coefficients)

# Вивід аналітичного вигляду функцій
print("Аналітичний вигляд функції попиту: ", demand_function)
print("Аналітичний вигляд функції пропозиції: ", supply_function)

# Побудова графіків
plt.figure(figsize=(10, 6))
plt.plot(prices, demand_function(prices), label='Попит', color='blue')
plt.plot(prices, supply_function(prices), label='Пропозиція', color='green')
plt.xlabel('Ціна')
plt.ylabel('Кількість')
plt.title('Графік попиту та пропозиції')
plt.legend()
plt.grid(True)

# Знах точки ринкової рівноваги
equilibrium_price = np.roots(demand_coefficients - supply_coefficients)[0]
equilibrium_quantity = demand_function(equilibrium_price)

plt.scatter(equilibrium_price, equilibrium_quantity, color='red', label='Ринкова рівновага')
plt.legend()

# Дослідж стану рівноваги на стабільність
if demand_function(equilibrium_price) > supply_function(equilibrium_price):
    stability = 'Нестабільна'
else:
    stability = 'Стабільна'

print(f"Ринкова рівновага: Ціна = {equilibrium_price}, Кількість = {equilibrium_quantity}")
print(f"Стан рівноваги: {stability}")

# Зміни параметрів ринкової рівноваги після введення податку
tax = 0.4
new_prices = prices * (1 + tax)
new_demand_function = np.poly1d(np.polyfit(new_prices, demand, 1))
new_supply_function = np.poly1d(np.polyfit(new_prices, supply, 1))

new_equilibrium_price = np.roots(new_demand_function - new_supply_function)[0]
new_equilibrium_quantity = new_demand_function(new_equilibrium_price)

plt.scatter(new_equilibrium_price, new_equilibrium_quantity, color='orange', label='Нова рівновага з податком')
plt.legend()

print(f"Нова ринкова рівновага з податком: Ціна = {new_equilibrium_price}, Кількість = {new_equilibrium_quantity}")

# Вивід графіків
plt.show()
