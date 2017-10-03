"""
Write a python function to encrypt the given sentence as follows and return the encrypted message:
1. Words at odd positions  : Reverse it.
2. Words at even positions : Rearrange the characters so that all consonants appear before the vowels and their order should not change.
Sample Data:
Input : The sun rises in the east
Output : eht snu sesir ni eht stea
"""

def encryptMsg(sentence):
	words_list = sentence.split(" ")
	for i in range(0, len(words_list)):
		if (i+1)%2 !=0:
			# odd becaue this is the first word at 0th index
			# so reverse it.
			words_list[i] = words_list[i][::-1]
		else:
			# even
			temp_word = ""
			vowels = ""
			for char in words_list[i]:
				if char in ['a','A','e','E','i','I','o','O','u','U']:
					vowels += char
				else:
					temp_word += char
			words_list[i] = temp_word+vowels
	return ' '.join(words_list)


print(encryptMsg("The sun rises in the east"))