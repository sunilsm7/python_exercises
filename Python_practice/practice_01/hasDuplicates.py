"""
Write a function called has_duplicates that takes a list and returns True,
if there is any element that appears more than once.
It should not modify the original list.
"""
def checkDuplicates(list):
	new_list = []
	for item in list:
		if item not in new_list:
			new_list.append(item)
	return new_list

def hasDuplicates(list):
	# if len(list) != len(set(list)):
	# 	return False
	if len(list) != len(checkDuplicates(list)):
		return False
	return True


list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5,6,1]


test1 = hasDuplicates(list1)
test2 = hasDuplicates(list2)

print(test1)
print(test2)