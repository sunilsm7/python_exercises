"""
Given 2 ints, a and b, return their sum.
However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


sorta_sum(3, 4) == 7
sorta_sum(9, 4) == 20
sorta_sum(10, 11) == 21
"""

def sorta_sum(x, y):
	sum = x + y
	if sum in range(10,20):
		return 20
	else:
		return sum


def test_sorta_sum():
	assert sorta_sum(3, 4) == 7
	assert sorta_sum(9, 4) == 20
	assert sorta_sum(10, 11) == 21


test_sorta_sum()