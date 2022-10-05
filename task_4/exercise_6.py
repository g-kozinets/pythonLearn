
my_str = "In 1984 there were 13 instances of a protest with over 1000 people attending"
splited_list = my_str.split(" ")
my_list = list(int(x) for x in splited_list if x.isdigit())

print(my_list)
