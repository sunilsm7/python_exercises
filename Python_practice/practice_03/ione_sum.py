"""
Given 3 int values, a b c, return their sum.
However, if one of the values is the same as another of the values,
it does not count towards the sum.


lone_sum(1, 2, 3) == 6
lone_sum(3, 2, 3) == 2
lone_sum(3, 3, 3) == 0
"""

def lone_sum(x,y,z):
	sum = 0
	if x == y and x == z:
		return sum
	elif x == y:
		return z
	elif x == z:
		return y
	elif y == z:
		return x
	else:
		return x + y + z

lone_sum(1,2,3)

def test_lone_sum():
	assert lone_sum(1, 2, 3) == 6
	assert lone_sum(3, 2, 3) == 2
	assert lone_sum(3, 3, 3) == 0

test_lone_sum()


def lone_sum2(a, b, c):
  sum = 0
  if a != b and a != c: 
  	return sum += a
  if b != a and b != c:
  	return sum += b
  if c != a and c != b:
  	return sum += c