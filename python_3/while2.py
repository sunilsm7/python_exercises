"""
	break statement

break  statement allows to breakout out of the loop.
"""
count = 0
while count < 10:
	count +=1
	if count == 5:
		break
	print("inside while loop", count)

print("out of while loop")