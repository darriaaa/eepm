import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Визначення диференціального рівняння
def model(P, t):
    dP_dt = 0.004 * P * (P - 180)
    return dP_dt

# Початкові умови
P0_1 = 250  # Поч чис: 250 кролів
P0_2 = 120  # Поч чис: 120 кролів

t = np.linspace(0, 1, 100)  # час від 0 до 1 місяця

# Розв диф рівняння
P_1 = odeint(model, P0_1, t)
P_2 = odeint(model, P0_2, t)

# Визначення чисельності популяції в момент часу t = 1
P1_1 = P_1[-1][0]  
P1_2 = P_2[-1][0]  

print("Чисельність популяції в момент часу t = 1 для початкової чисельності 250 кролів:", P1_1)
print("Чисельність популяції в момент часу t = 1 для початкової чисельності 120 кролів:", P1_2)

# Графік
plt.figure(figsize=(10, 6))
plt.plot(t, P_1, 'r-', linewidth=2, label='Поч. чисельність: 250')
plt.plot(t, P_2, 'b--', linewidth=2, label='Поч. чисельність: 120')
plt.title('Динаміка популяції кролів')
plt.xlabel('Час (місяці)')
plt.ylabel('Чисельність популяції')
plt.legend()
plt.grid(True)
plt.show()
