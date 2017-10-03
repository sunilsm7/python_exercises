"""
Write a Python program for Binary Search.
"""

def binary_sort(sortedlist,n,x):
	sortedlist = listSorted(sortedlist)
	start = 0
	end = n - 1
	while(start <= end):
		mid = (start + end)//2
		if (x == sortedlist[mid]):
			return mid
		elif(x < sortedlist[mid]):

			end = mid - 1
		else:
			start = mid + 1 
	 
	return -1


def listSorted(mylist):
	n = len(mylist)
	for i in range(n):
		for j in range(1, n-i):
			if mylist[j-1] > mylist[j]:
				# do a tuple swap
				(mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
	return mylist



n = int(input("Enter the size of the list: "))

sortedlist = []

for i in range(n):
 sortedlist.append(input("Enter {}th element: ".format(i)))

x = input("Enter the number to search: ")
position = binary_sort(sortedlist, n, x)

if(position != -1):
 print("Entered number {} is present at position: {}".format(x,position))
else:
 print("Entered number {} is not present in the list".format(x))