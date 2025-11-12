import random

#s_1 = {random.randint(1, 100) for i in range(7)}
#print(f"Первое множество: {s_1}")
#s_2 = {random.randint(1, 100) for i in range(5)}
#print(f"Второе множество: {s_2}")

s_1 = {1,2,3,4,5,6,7,8,9,10}
s_2 = {1,2,3}

i = s_2.intersection(s_1)

if i==s_2:
    print("Второе множество является подмножеством первого")
else:
    print("Второе множество не является подмножеством первого")