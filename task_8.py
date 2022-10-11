# ex1
list_str = ["qwe", "rty", "uiop", "asdv", "gerge", "agerg"]


# ex2
def add_prefix(str2):
    return "prefix_" + str2


edited_list = list(map(add_prefix, list_str))

print(edited_list)


# ex3
def filter_str(value):
    return list(value)[0] == "a"


filtered_list = list(filter(filter_str, list_str))
print(filtered_list)

# ex4
t1 = (324, 435, 456, 567)
t2 = ('fsd', 'gregr', 'gfdgf', 'fdg')
t3 = ("1", "2", "3", "4")

list_t = [t1, t2, t3]

for tup in list_t:
    for item in tup:
        print(item)

# ex5
list01 = [1, 2, 3, 4, 5]
list02 = [34, 54, 0]

for (i, j) in zip(list01, list02):
    print("i + j = " + str(i + j))

# ex7
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index, value in enumerate(my_list):
    if (index + 1) % 3 == 0:
        print(str(value) + str(value))
    else:
        print(value)

