N = int(input("Введите количество чисел: "))
print("Четные числа: ")
for i in range(1,N+1,1):
    if i % 2 == 0:
        print(i)