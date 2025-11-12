N = int(input("Введите число: "))
count = 0
for i in range(1,N+1,1):
    if N % i == 0:
        count+=1
print(f"Количество делителей числа {N}: {count}")