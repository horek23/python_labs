import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(10, 10)

fig, ax = plt.subplots()

im = ax.imshow(data, cmap='viridis')

fig.colorbar(im, ax=ax)

ax.set_title("Тепловая карта 10×10")

plt.tight_layout()
plt.savefig('example_plot.png', dpi=300)
plt.savefig('example_plot.pdf', dpi=300)
plt.show()