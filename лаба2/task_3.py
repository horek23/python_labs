import random

d_1 = {f"key{i}": random.randint(1, 100) for i in range(5)}
d_2 = {f"key{i}": random.randint(1, 100) for i in range(3,7,1)}

print(f"Первый словарь: {d_1.items()}")
print(f"Второй словарь: {d_2.items()}")

common_keys = d_1.keys() & d_2.keys()
print(f"Значения совпадающих ключей: ")
for key in common_keys:
    print(d_1.get(key),d_2.get(key))