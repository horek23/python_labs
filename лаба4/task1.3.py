import numpy as np
import matplotlib.pyplot as plt

sizes = [5,15,30,23,12]
labels = ['Сыр', 'Краб', 'Cметана и зелень', 'Соль', 'Лобстер']

fig, ax1 = plt.subplots()

plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title("Предпочтения потребиетлей во вкусах чипсов",fontsize=19)
plt.tight_layout()
plt.savefig('example_plot.png', dpi=300)
plt.savefig('example_plot.pdf', dpi=300)
plt.show()