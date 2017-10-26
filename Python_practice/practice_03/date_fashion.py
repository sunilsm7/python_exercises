"""
You and your date are trying to get a table at a restaurant.
The parameter "you" is the stylishness of your clothes, in the range 0..10,
and "date" is the stylishness of your date's clothes.
The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes.
If either of you is very stylish, 8 or more, then the result is 2 (yes).
With the exception that if either of you has style of 2 or less, then the result is 0 (no).
Otherwise the result is 1 (maybe).


date_fashion(5, 10) -> 2
date_fashion(5, 2) -> 0
date_fashion(5, 5) -> 1
"""

def number_to_choice(number):
	return {0:'no', 1:'maybe', 2:'yes'}[number]

def date_fashion(your_stylishness, your_date_stylishness):
	if your_stylishness <= 2 or your_date_stylishness <= 2:
		return number_to_choice(0)
	elif (your_stylishness >= 8 and your_stylishness <= 10) or (your_date_stylishness >= 8 and your_date_stylishness <= 10):
		return number_to_choice(2)
	else:
		return number_to_choice(1)

# test = date_fashion(5, 10)
# print(test)

def test_date_fashion():
	assert date_fashion(5, 10) == 'yes'
	assert date_fashion(5, 2) == 'no'
	assert date_fashion(5, 5) == 'maybe'

test_date_fashion()