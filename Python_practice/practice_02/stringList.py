"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

def checkPalindrome(str):
	if str == str[::-1]:
		return "Its palindrome"
	return "Its not palindrome"


str = input('Enter string:')

result = checkPalindrome(str)
print(result)
