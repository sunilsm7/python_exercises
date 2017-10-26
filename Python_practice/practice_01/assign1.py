"""
	list = [4,5,1,38, 98, 77, 34,66,88, 55] 
	accept input number and return all lesser number in list.	
"""

list = [4,5,1,38, 98, 77, 34,66,88, 55]
num = int(input('Enter number:'))

# Solution 1
def checkNumPresent(list):
	newList = []
	for n in range(len(list)):
		#print("number {} at index {}".format(list[n], n))
		if num > list[n]:
			newList.append(list[n])
	return newList


# Solution 2
def testNumPresent(list):
	newList = [n for n in list if num > n]
	return newList


result = checkNumPresent(list)
print(result)

print(testNumPresent(list))