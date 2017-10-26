"""
validate mobile number.
consider the following conditions.
	1. accept Digits only 
	2. 10 digits only.
	3. Starts with the following series only [70......99]
	4. Should not start with [0.......69]

extra complexity validate using regular expression.
"""
import re

def mobile_number_validate(mobile):
	#mobile_str = str(mobile)
	#regex = r"^\d{10}$"
	regex = r"^(\+\d{1,3}[- ]?)?\d{10}$"
	test = re.compile(regex)
	if not test.search(mobile):
		return "invalid number"
	else:
		return "valid number"

num = '+91-1087339090'
result = mobile_number_validate(num)
print(result)