"""
Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference
"""
import math

def diff_number(num):
	if num > 17:
		diff = (num - 17) * 2
		return diff
	return 17 - num

result = diff_number(2)
print(result)