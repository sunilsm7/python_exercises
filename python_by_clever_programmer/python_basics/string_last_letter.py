"""
    Write a function last_letter that returns the
    last letter of a string

    Note: use return and not print in function.
    ex. last_letter('hello!') #-- > !

"""
def last_letter(my_string):
    return my_string[-1]

def test_last_letter():
    assert last_letter('hello!') == '!'
    assert last_letter('banana') == 'a'
    assert last_letter('101') == '1'
    assert last_letter('pokemon') == 'n'
    print('Your code is correct!')

test_last_letter()

print(last_letter('hello'))