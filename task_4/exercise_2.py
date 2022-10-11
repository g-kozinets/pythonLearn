my_list = [x/3 if x % 3 == 0 else int(str(x) + str(x)) for x in range(1, 1000)]
print(my_list)
