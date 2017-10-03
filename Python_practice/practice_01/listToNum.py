"""
Write a python code to convert a list of integers  into a comma separated string.
Ex .   [1,2,3,4,5,6] should be converted to  "1,2,3,4,5,6".
"""

def listNumToString(list):

	return ", ".join([str(item) for item in list])


list = [1,2,3,4,5,6]

result = listNumToString(list)

print(result)