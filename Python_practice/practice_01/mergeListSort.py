"""
Write a python program which merges the content of 2 lists , sorts the merged list and removes the element which is repeated maximum number of times.
Note : The lists should be merged such that the first element of list1 should be taken followed by the first element of the list2. 
At the end, if there are any elements left, append it to the merged list.
sample_input : [1,2,3,4,1] [2,3,4,5,4,6]
Merged_list : [1, 2, 2, 3, 3, 4, 4, 5, 1, 4, 6]
After Sorting: [1,1,2,2,3,3,4,4,4,5,6]
After Removing Duplicates: [1,1,2,2,3,2,5,6]
You may write the following functions to achieve the above functionalities
1. def merge_lists(list1,list2)
2. def sort_list(merged_list)
3. def remove_max_duplicate_element(sorted_merged_list)
Note: If 2 or more numbers in the list have the maximum occurances, remove all those numbers from the list.
"""

def mergeList(list1, list2):
	temp_list = []
	if len(list1) > len(list2):
		longer_list = list1
		smaller_list = list2
	else:
		longer_list = list2
		smaller_list = list1

	count = 0
	# print len(smaller_list)

	for i in range(0, len(smaller_list)):
		temp_list.append(list1[i])
		count +=1
		temp_list.append(list2[i])
		count += 1
	temp_list.extend(longer_list[len(smaller_list):])
	return temp_list
list1 = [1,2,3,4,1]
list2 = [2,3,4,5,4,6]

mergeList = mergeList(list1, list2)
print(mergeList)

def sortList(mergeList):
	mergeList.sort()
	return mergeList
	

sortedMergedList = sortList(mergeList)
print(sortedMergedList)

def removeMaxDuplicateElements(sortedMergedList):
	x = {}
	new_list = []
	for item in sortedMergedList:
		if item not in x:
			x[item] = 1
		else:
			x[item] += 1
	max_count = max(x.values())
	for k,v in x.items():
		
		if v == max_count:
			#print("removing {}".format(k))
			for item in sortedMergedList:
				if item == k:
					sortedMergedList.remove(item)
				else:
					new_list.append(item)
	return new_list

finalResult = removeMaxDuplicateElements(sortedMergedList)
print(finalResult)


