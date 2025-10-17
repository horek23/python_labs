print("Введите строку: ")
text = input()

vowels = "aeiou"

i=0
while i < len(text):
    if text[i] not in vowels:
        print(text[i], end="")
    i = i + 1
