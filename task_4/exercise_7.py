odd_str = "odd"
even_str = "even"


my_list = [
    even_str
    if x % 2 == 0
    else odd_str
    for x in range(1, 20)
]

print(my_list)
