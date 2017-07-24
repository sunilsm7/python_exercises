"""
    write a function is_even that takes
    in a number and returns True if it is even,
    otherwise False.

"""

def test_is_even(number):
    # if number % 2 == 0:
    #     return True
    # else:
    #     return False
    return number % 2 == 0

# print(test_is_even(3))
# print(test_is_even(4))
# print(test_is_even(8))

def is_odd(number):
    return number % 2 != 0

print(is_odd(3))