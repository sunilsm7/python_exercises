"""
Write a function group() to split list and create new lists according to input
"""
import math

list = [1,2,3,4,5,6,7,8,9,10,11,12]

def group_list(list, n):
	length = len(list)
	temp = length // n
	ot = int(math.ceil(float(length)/n))
	return list[:temp], list[temp:length-ot], list[length-ot:]



result = group_list(list, 3)
print(result)