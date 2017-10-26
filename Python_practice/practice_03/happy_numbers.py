"""
Happy Numbers - A happy number is defined by the following process.
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.
Display an example of your output here. Find first 8 happy numbers.
"""
def sum_of_digits(num):
	digits_sum = 0
	temp = num
	while(temp > 0):
		r = temp % 10
		digits_sum +=  r ** 2
		temp = temp / 10
	return digits_sum


def happy_number(num_list):
	happy_number_list = []
	unhappy_number_list = []
	for num in num_list:
		temp = num
		while(temp >= 10):
			temp = sum_of_digits(temp)
		if temp == 1:
			#return 'Happy Number: {}'.format(num)
			happy_number_list.append(num)
		else:
			#return 'Unhappy Number: {}'.format(num)
			unhappy_number_list.append(num)
	return happy_number_list, unhappy_number_list

num_list = range(101)
result = happy_number(num_list)
print("happy number list:", result[0])
print("Unhappy number list:",result[1])
