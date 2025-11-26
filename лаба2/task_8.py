import random

numbers = tuple(random.randint(1, 100) for _ in range(5))
print(f"Кортеж: {numbers}")
numbers = list(numbers)
for num in numbers:
    if num % 3 != 0:
        numbers.append(num)
numbers = tuple(numbers)
print(f"Новый кортеж: {numbers}")