"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point
 - we’ll get to it soon)

"""
import random 

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Randomly generate two list
list3 = [random.randrange(0,30,1) for i in range(0,30,1)]
list4 = [random.randrange(0,30,1) for i in range(0,30,1)]

# to sort the result
def sortedList(mylist):
	n = len(mylist)
	for i in range(n):
		for j in range(1, n-i):
			# sort by ascending order. to descending order use <
			if mylist[j-1] > mylist[j]:
				# do a tuple swap
				(mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
	return mylist

def listOverlap(list1,list2):
	new_list = []
	for count in range(len(list1)):
		if list1[count] in list2 and list1[count] not in new_list:
			new_list.append(list1[count])
	return sortedList(new_list)

result = listOverlap(list3, list4)
print(result)