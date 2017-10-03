"""
	continue statement

When continue  statement encountered in the loop, 
it ends the current iteration and programs control goes to the end of the loop body.
"""
count = 0

while count < 10:
	count += 1
	if count %2 == 0:
		continue
	print(count)


