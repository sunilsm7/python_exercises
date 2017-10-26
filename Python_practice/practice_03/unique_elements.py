"""
Write a function unique to find all the unique elements of a list.
"""

def unique_ele(list):
	new_list = []
	for i in list:
		if i not in new_list:
			new_list.append(i)
	return new_list

list = [1,2,3,1,4,3,7,5,8,5,8,4,3]
result = unique_ele(list)
print(result)