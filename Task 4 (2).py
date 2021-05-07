my_str = input("Введите несколько слов, разделенных пробелами: ")
for ind, el in enumerate(my_str.split(" "),1):
    if len(el) <= 10:
        print(ind , el)
    else:
        print(ind , el[:10])