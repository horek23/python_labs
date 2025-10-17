print("Введите число: ")
a=int(input())

if a % 7==0:
    print("Магическое число: ")
else:
    sum=0
    while a>0:
        sum=sum + a%10
        a=a//10
    print(sum)
