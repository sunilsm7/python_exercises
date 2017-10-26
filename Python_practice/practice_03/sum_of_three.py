"""
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return thrice of their sum
"""

def sum_of_nums(num1, num2, num3):
	if num1 == num2 == num3:
		return (num1+num2+num3) * 3
	return num1+num2+num3

result = sum_of_nums(14,14,14)
print(result)
