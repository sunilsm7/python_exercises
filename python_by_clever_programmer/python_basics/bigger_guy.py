"""
    write a function bigger_guy that takes
    in two numbers and returns the bigger one.abs
"""

def bigger_guy(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2

def test_bigger_guy():
    assert bigger_guy(1,2) == 2
    assert bigger_guy(10,20) == 20
    assert bigger_guy(2,1) == 2
    #assert bigger_guy(1,2) == 2
    print("Your code is correct")

test_bigger_guy()
print(bigger_guy(12,13))