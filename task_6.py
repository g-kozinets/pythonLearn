import random


def check_input():
    my_input = random.randrange(1, 4)
    if my_input == 1:
        raise ArithmeticError("ArithmeticError")
    elif my_input == 2:
        raise AssertionError("AssertionError")
    elif my_input == 3:
        print(3 / 0)


try:
    check_input()
except (ArithmeticError, ZeroDivisionError, AssertionError) as e:
    print(e)
