import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define a função da EDO
def edo(x, y):
    return x - 2*y

# Define o intervalo de x -> (t_0,T)
x_span = (-5,5)

# Define a condição inicial -> y(t_0)
y0 = [4]

# Resolve a EDO
sol = solve_ivp(edo, x_span, y0, t_eval=np.linspace(x_span[0], x_span[1], 1000))

# Calcula a concavidade
dy_dx = sol.y[0]
d2y_dx2 = np.gradient(dy_dx, sol.t)
concavity = np.sign(d2y_dx2)

# Plot da solução e concavidade
plt.plot(sol.t, sol.y[0], color='black', label='Solução da EDO')
plt.plot(sol.t, concavity, color='black', label='Concavidade', linestyle='--')
plt.xlabel('x')
plt.ylabel('y(x) e concavidade')
plt.title('Solução da EDO e Concavidade')
plt.legend()
plt.grid(True)
plt.show()
