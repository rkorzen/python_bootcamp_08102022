import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 300)
y = np.floor(x)
y2 = x ** 2
plt.plot(x, y, marker="+",label="floor(x)")
plt.plot(x, y2, c="r", label=r"$x^2$")
plt.legend()
plt.show()
