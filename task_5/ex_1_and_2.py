class MyError(Exception):
    pass


hello_str = 'Hello'


def check_input():
    my_input = int(input("Enter 1, 2 or 3\n"))
    if my_input == 1:
        raise MyError(hello_str)
    elif my_input == 2:
        raise MyError("By")
    elif my_input == 3:
        print("You god damn right")


try:
    check_input()
    print("correct")
except MyError as e:
    if hello_str == e:
        print(hello_str)
    else:
        raise MyError
