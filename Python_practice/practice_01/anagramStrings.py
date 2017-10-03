"""
Write a python function to detect if 2 strings are anagrams.
"""
def sortedList(mylist):
	n = len(mylist)
	for i in range(n):
		for j in range(1, n-i):
			if mylist[j-1] > mylist[j]:
				# do a tuple swap
				(mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
	return mylist

def isAnagram(str1,str2):
	if len(str1) != len(str2):
		#print("lenghts are not equal")
		return False

	if sortedList(list(str1)) == sortedList(list(str2)):
		# or sorted(list(str1)) == sorted(list(str2))
		#print("Anagrams strings")
		return True
	else:
		#print("strigs are not anagrams")
		return False

str1 = input('String1:')
str2 = input('String2:')
result = isAnagram(str1, str2)

if result == True:
	print("its anagrams")
else:
	print("its	not anagrams")

