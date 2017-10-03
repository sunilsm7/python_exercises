"""
Program in Python to print numbers in a range (m,n) without using any loops.
"""

def printNumbers(start,end):
	if start == end:
		return end
	elif start > end:
		print("Incorrect range")

	if start < end:
		print(start)
		return printNumbers(start+1, end)


result = printNumbers(1,10)
print(result)
