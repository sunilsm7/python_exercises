"""
    write a function biggest_guy that takes in
    three numbers as input and returns the biggest one.
"""
def bigger_guy(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def biggest_guy(num1, num2, num3):
    # find bigger guy between num1 and num2
    # find biggest guy between bigger guy and num3
    return bigger_guy(bigger_guy(num1, num2), num3)
    #return max(num1, num2, num3)


# def biggest_guy(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3

def test_biggest_guy():
    print('------Running Tests------')
    assert biggest_guy(1,2,3) == 3
    assert biggest_guy(10,20,30) == 30
    assert biggest_guy(11,12,13) == 13
    assert biggest_guy(13,44,23) == 44
    print('Success')
    print('Your code is correct')

test_biggest_guy()
print(biggest_guy(1,2,3))