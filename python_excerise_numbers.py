import matplotlib.pyplot as plt
import math
import numpy as np

t = np.linspace(0, 50, 10000)

A1, f1, p1, d1 = 1, 2, math.pi / 2, 0.01
A2, f2, p2, d2 = 1, 3, math.pi / 4, 0.012

x = A1 * np.sin(f1 * t + p1) * np.exp(-d1 * t)
y = A2 * np.sin(f2 * t + p2) * np.exp(-d2 * t)

plt.figure(figsize=(8, 8))
plt.plot(x, y, linewidth=0.5)
plt.title("Harmonograph Simulation")
plt.axis("equal")
plt.axis("off")
plt.show()