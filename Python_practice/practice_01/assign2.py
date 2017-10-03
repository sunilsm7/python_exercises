"""
	list = [1,5,3,7,1,2,4,7,4,3,8,4,6,9,2,4,2] find the frequency of occurrences of numbers and return it dictionary.
	dict = {1:2, 3:2,...}
	and sort dictionary according to highest occurrence of numbers
	dict = {4:4, 2:3,....}
"""

list = [1,5,3,7,1,2,4,7,4,3,8,4,6,9,2,4,2]



def checkResult(list):
	dict = {}
	for n in list:
		dict[n] = list.count(n)
	return dict


result = checkResult(list)
#print(result)

def returnDict(result):
	list = [n for n in result.values()]
	for k in result:
		print("key:{} value:{}".format(k,result[k]))
	return result

print(returnDict(result))
