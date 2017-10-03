"""
Write a for loop that iterates over a list of numbers 1st and prints the numbers in the list whose square is divisible by 8. 
For example, if 1st is [2,3,4,5,6,7,8,9], then the output should be : 4 8
"""

def numDivisibleBy(list):
	new_list = []

	for n in list:
		if (n**2)%8 == 0:
			new_list.append(n)
	return new_list


list = [2,3,4,5,6,7,8,9]

result = numDivisibleBy(list)

print(result)