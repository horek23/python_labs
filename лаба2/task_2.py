import random

numbers = [random.randint(1, 100) for _ in range(5)]

print("Сгенерированный список чисел: ")
for number in numbers:
    print(number, end=" ")

print()

mean = sum(numbers) / len(numbers)
print(f"Среднее арифметическое значение: {mean}")
