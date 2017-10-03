"""
Python program to find the number of occurances of each character in a string.
"""

def charOccurance(str):
	dictResult = {}
	for item in str:
		if item != "":
			if item in dictResult.keys():
				dictResult[item] += 1
			else:
				dictResult[item] = 1
	return dictResult

ipStr = input('Enter string:')
result = charOccurance(ipStr)
print(result)