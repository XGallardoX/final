import numpy as np
import matplotlib.pyplot as plt

# Generar valores x
x = np.linspace(0, 2 * np.pi, 100)
print(x)
# Calcular valore
# s y para funciones trigonométricas
y_sin = np.sin(x)
print(y_sin)
# Graficar las funciones trigonométricas
plt.plot(x, y_sin, label='sin(x)')


# Configurar los ejes y la leyenda
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Mostrar la gráfica
plt.show()
