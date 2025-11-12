lst = [1,2,9,1,1,7,8,9]

new_lst = []
for num in lst:
     if lst.count(num) == 1:
         new_lst.append(num)

print(new_lst)
