"""
	accept only 0, 1 and 2 values and return sorted list without using sort function.
	input: [0,1,2,0,2]
	output: [0,0,1,2,2]
"""
list = []

try:
	n = int(input('How many numbers:'))
	i = 0
	while(i < n):
		num = int(input('Enter numbers(only 0,1,2) :'))
		if num not in(0,1,2):
			raise ValueError()
		list.append(num)	
		i +=1
except:
	print("Enter only 0's, 1's, 2's ")

print(list)

def sortedList(mylist):
	n = len(mylist)
	for i in range(n):
		for j in range(1, n-i):
			if mylist[j-1] > mylist[j]:
				# do a tuple swap
				(mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
	return mylist

print(sortedList(list))
