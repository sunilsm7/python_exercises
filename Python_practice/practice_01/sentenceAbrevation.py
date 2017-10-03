"""
Write a python function which accepts a sentence and
converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence.
Rules to follow while shortening:
A. Spaces are to be retained as is, i.e. even multiple spaces are to be retained.
B. Each word should be encoded separately
		- If a word has only vowels then retain the word as is.
		- If a word has a consonant (at least 1 ) then retain only those consonants.
Example:
	Input 1 :
		I love India
	Output 1 :
		I lv nd
	Input 2 :
		MSD says I love cricket and tennis too
	Output 2 :
		MSD sys I lv crckt nd tnns t
	Input 3 : 
		I will not repeat mistakes
	Output 3:
		I wll nt rpt mstks
"""

"""
Solution:
1. 	Split the sentence based on a single space to create a list of words.
2.	Individually check if each word is made of only vowels or not.
3.	If No, then remove the vowels, we can use regulat expressions to do that.
	re.sub(r'<the_pattern>','<replaced_with','<the_string>')
	replace the pattern in first argument with the second argument.
4. Join them back to form the sentence.

"""

import re

def is_all_vowels(word):
	count = 0
	for item in word:
		if item in ['a','A','e','E','i','I','o','O','u','U']:
			count += 1
	if count == len(word):
		return True
	else:
		return False

def compress(msg):
	words_list = msg.split(' ') # this returns the spaces
	for i in range(0, len(words_list)):
		word = words_list[i]
		if not is_all_vowels(word):
			words_list[i] = re.sub(r"[aAeEiIoOuU]","", word)
	print(words_list)
	return " ".join(words_list)

print(compress("I will not repeat mistakes"))