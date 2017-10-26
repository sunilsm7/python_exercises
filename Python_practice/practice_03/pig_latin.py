"""
Pig Latin - Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).
Read Wikipedia for more information on rules.
"""

def check_vowel(s):
	if s.lower() not in ('a','e','i','o','u'):
		return True
	return False

def pig_latin(string):
	#start_letter = string[0]
	if check_vowel(string[0]) == True and check_vowel(string[1]) == True:
		return string[2:] + string[0:2] + "ay"
	elif check_vowel(string[0]) == True:
		return string[1:] + string[0] + "ay"
	else:
		return string + 'yay'


test1 = pig_latin('sunil')
test2 = pig_latin('input')
test3 = pig_latin('cheers')
print(test1)
print(test2)
print(test3)

def test_pig_latin():
	assert pig_latin('sunil') == 'unilsay'
	assert pig_latin('input') == 'inputyay'
	assert pig_latin('cheers') == 'eerschay'


test_pig_latin()