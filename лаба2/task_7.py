import random

N = int(input("Введите количество ключей: "))

d_1 = {f"key{i}": i**2 for i in range(1,N+1,1)}

print(f"Словарь: {d_1.items()}")