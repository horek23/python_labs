import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)

y1 = x**2 - 4 * x + 3
y2 = np.sin(x)

fig, ax1 = plt.subplots()

ax1.plot(x, y1, label="f1(x) = x^2 - 4x + 3",color='b')
ax1.set_xlabel("x")
ax1.set_ylabel("f1(x)")
ax1.grid(True)

ax2 = ax1.twinx()

ax2.plot(x, y2, linestyle="--", label="f2(x) = sin(x)",color='r')
ax2.set_ylabel("f2(x)")

ax1.legend(loc='upper center', bbox_to_anchor=(0.65, 1))
ax2.legend(loc='upper center', bbox_to_anchor=(0.65, 0.9))

idx_min_y1 = np.argmin(y1)
ax1.annotate(
    "Минимум f1",
    xy=(x[idx_min_y1], y1[idx_min_y1]),
    xytext=(x[idx_min_y1] + 0.3, y1[idx_min_y1] + 3),
    arrowprops=dict(arrowstyle="->")
)

ax2.annotate(
    "Точка f2 при x=0",
    xy=(0, y2[0]),
    xytext=(1, 0.5),
    arrowprops=dict(arrowstyle="->")
)

plt.title("Две функции с разными осями Y",fontsize=19)
plt.tight_layout()
plt.savefig('example_plot.png', dpi=300)
plt.savefig('example_plot.pdf', dpi=300)
plt.show()