
my_str = "The trickiest part of learning list comprehension for me was really understanding the syntax."
splited_list = my_str.split(" ")
my_list = list(x for x in splited_list if len(x) < 4)

print(my_list)
