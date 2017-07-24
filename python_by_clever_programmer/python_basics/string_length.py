"""
    Write a function string_length that takes in a
    string and returns its length.
    Hint:

"""

def string_length(my_string):
    count = 0
    for letter in my_string:
        print(letter, end=' ')
        count += 1 # increment count by 1

    return count
   
    
print(string_length('hello!'))

def test_string_length():
    assert string_length('hello!') == 6
    assert string_length('banana') == 6
    assert string_length('funnyguys') == 9
    assert string_length('101') == 6
