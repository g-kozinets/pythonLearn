
my_str = "hi, 3.44, 535"
splited_list = my_str.split(", ")
index = 0
my_list = list((i, x) for i, x in enumerate(splited_list))

print(my_list)
