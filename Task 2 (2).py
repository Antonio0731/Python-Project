my_list = list(input("Заполните список произвольными элементами: "))
print(my_list)
for ind , el in enumerate(my_list):
    if ind % 2 != 0 and ind != len(my_list):
        my_list[ind-1],my_list[ind] = my_list[ind],my_list[ind-1]
    else:
        my_list[ind] = my_list[ind]


#m_list[i],my_list[i+1], my_list[i+2],my_list[i+3]=my_list[i+1],my_list[i],my_list[i+3],my_list[i+2]
print(my_list)