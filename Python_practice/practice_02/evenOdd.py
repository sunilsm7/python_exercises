"""
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
"""

def evenOdd(num):
	if num%2 != 0:
		return "Odd number"
	return "Even number"

num = int(input('Enter number:'))

result = evenOdd(num)
print(result)

