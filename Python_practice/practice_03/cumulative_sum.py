"""
cumulative sum of list integers
"""

def cumulative_sum(list):
	new_list = []
	sum = 0
	for i in list:
		sum += i
		new_list.append(sum)
	return new_list

result = cumulative_sum([1,2,3,4,5,6])
print(result)