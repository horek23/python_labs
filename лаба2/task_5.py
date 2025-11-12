N = int(input("Введите количество строк в списке: "))
lst = []
for i in range(N):
    str = input(f"Введите {i} строку: ")
    lst.append(str)

min_len = len(lst[0])
for str in lst:
    min_len = min(min_len, len(str))
print(f"Длина самой короткой строки: {min_len}")