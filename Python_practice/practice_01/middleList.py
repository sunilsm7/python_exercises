"""
Write a python function called middle that takes a list and returns a new list that contains all but the first and last elements.
So middle([1,2,3,4]) should return [2,3].
"""

def middleList(list):

	return list[1:-1] 		#list[1:len(list)-1]


list = [1,2,3,4]

result = middleList(list)

print(result)