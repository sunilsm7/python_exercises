"""
Write a python function called remove_duplicates that takes a list and
returns a new list with only the unique elements from the original.
"""

def removeDuplicates(list):
	new_list = []
	for item in list:
		if item not in new_list:
			new_list.append(item)
	return new_list


list = [1,2,3,1,1,2,8,5,3,6,4,9,7,6,4,3]
print(list)
result = removeDuplicates(list)

print(result)