"""

Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.

near_ten(12) == True
near_ten(17) == False
near_ten(19) == True
"""

def near_ten(num):
	rem = num % 10	
	if rem <= 2 or (10-rem) <= 2 :
		return True
	else:
	  return False





def test_near_ten():
	assert near_ten(12) == True
	assert near_ten(17) == False
	assert near_ten(19) == True

test_near_ten()
