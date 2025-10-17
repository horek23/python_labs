print("Введите фамилию, имя и отчество: ")
fio = input()
parts = fio.split()

while len(parts) < 3:
    print("Ожидается 3 слова, попробуйте еще раз: ")
    fio = input()
    parts = fio.split()

surname = parts[0].capitalize()
name = parts[1]
patronymic = parts[2]

initials = f"{name[0].upper()}.{patronymic[0].upper()}."
print(f"{surname} {initials}")