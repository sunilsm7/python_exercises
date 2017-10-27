"""

We want to make a row of bricks that is goal inches long.
We have a number of small bricks (1 inch each) and big bricks (5 inches each).
Return True if it is possible to make the goal by choosing from the given bricks.
This is a little harder than it looks and can be done without any loops.

make_bricks(3, 1, 8) == True
make_bricks(3, 1, 9) == False
make_bricks(3, 2, 10) == True
"""


def make_bricks(small, big, goal):
	if(goal > big*5+small):
		return False
	if (goal%5 > small):
		return False
	return True

def test_make_bricks():
	assert make_bricks(3, 1, 8) == True
	assert make_bricks(3, 1, 9) == False
	assert make_bricks(3, 2, 10) == True

	assert make_bricks(3, 2, 8) == True
	assert make_bricks(3, 2, 9) == False
	assert make_bricks(1, 4, 11) ==  True
	assert make_bricks(0, 3, 10) == True


test_make_bricks()