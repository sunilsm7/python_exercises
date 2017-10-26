"""
Write a function dups to find all duplicates in the list.
"""

def check_duplicates(list):
	new_list = []
	duplicates = []
	for i in list:
		if i not in new_list:
			new_list.append(i)
		else:
			duplicates.append(i)
	return duplicates


list = [1,2,3,1,4,3,7,5,8,5,8,4,3]
result = check_duplicates(list)
print(result)