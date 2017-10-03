"""
    Palindrome String
    original and reverse sting must be same.
    ex.
    input:aba
    output:aba
"""

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == text[::-1]

text = input("Enter a text:")
if is_palindrome(text):
    print("It's palindrome")
else:
    print("It's not palindrome")