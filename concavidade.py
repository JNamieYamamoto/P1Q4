import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def EDO(y, x):
    return x - 2*y

y0 = 4  # y(x_0)
x = np.linspace(-5, 5, 1000)  # Valores de x

# Resultado da EDO
sol = odeint(EDO, y0, x)

# Calculando a segunda derivada
dy_dx = sol[:, 0]  # y(x)
d2y_dx2 = np.gradient(dy_dx, x)

# Determinando a concavidade
concavity = np.sign(d2y_dx2)

# Plot da solução e concavidade
plt.plot(x, dy_dx, label='Exact Solution')
plt.plot(x, concavity, label='Concavity')
plt.xlabel('x')
plt.ylabel('y and Concavity')
plt.title('Exact Solution and Concavity of the ODE')
plt.legend()
plt.grid(True)
plt.show()
