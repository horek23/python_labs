print("Введите сумму: ")
banknote=int(input())

count_100= banknote//100
print(f"{count_100} по 100 рублей")
count_50=(banknote-count_100*100)//50
print(f"{count_50} по 50 рублей")
count_10=(banknote-count_100*100-count_50*50)//10
print(f"{count_10} по 10 рублей")
count_5=(banknote-count_100*100-count_50*50-count_10*10)//5
print(f"{count_5} по 5 рублей")
count_2=(banknote-count_100*100-count_50*50-count_10*10-count_5*5)//2
print(f"{count_2} по 2 рубля")
count_1=(banknote-count_100*100-count_50*50-count_10*10-count_5*5-count_2*2)
print(f"{count_1} по 1 рублю")