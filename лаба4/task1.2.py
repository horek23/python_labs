import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(3, 0.5, 50)

x2 = np.random.normal(1, 0.5, 50)
y2 = np.random.normal(2, 0.5, 50)

x3 = np.random.normal(5, 0.5, 50)
y3 = np.random.normal(5, 0.5, 50)

fig, ax1 = plt.subplots()

plt.scatter(x1, y1, color='blue')
plt.scatter(x2, y2, color='red')
plt.scatter(x3, y3, color='green')

plt.title("Три кластера нормального распределения",fontsize=19)
plt.tight_layout()
plt.savefig('example_plot.png', dpi=300)
plt.savefig('example_plot.pdf', dpi=300)
plt.show()