import random

numbers = tuple(random.randint(1, 100) for _ in range(5))
print(f"Кортеж: {numbers}")
new_numbers = ()
for num in numbers:
    if num % 3 != 0:
        new_numbers += (num,)
print(f"Новый кортеж: {new_numbers}")