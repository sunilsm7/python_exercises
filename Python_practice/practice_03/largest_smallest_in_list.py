"""
	Write a Python program to get the largest number from a list
"""

def largest_num_in_list(num_list):
	largest = num_list[0]
	for num in num_list:
		if num > largest:
			largest = num
	return largest


def smallest_num_in_list(num_list):
	smallest = num_list[0]
	for num in num_list:
		if num < smallest:
			smallest = num
	return smallest


num_list = [23,11,32,12,45,43,76,56,87,99]

largest = largest_num_in_list(num_list)
smallest = smallest_num_in_list(num_list)
print('Largest number:{}'.format(largest))
print('Smallest number:{}'.format(smallest))