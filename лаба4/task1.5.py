import numpy as np
import matplotlib.pyplot as plt

categories = ['Пепси', 'Фанта', 'Спрайт']
values = [123,112,97]
fig, ax = plt.subplots()

plt.bar(categories, values,color='green')

ax.set_title("Столбчатая диаграмма напитков")

plt.tight_layout()
plt.savefig('example_plot.png', dpi=300)
plt.savefig('example_plot.pdf', dpi=300)
plt.show()