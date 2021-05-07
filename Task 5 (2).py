my_list = [10, 7, 6, 6, 4, 3, 2, 2]
new = int(input("Введите цифру/число для добавления в список:"))
i = 0
for j in my_list:
    if new <= j:
        i += 1
my_list.insert(i,new)
print(my_list)