"""
python program to replace all the vowels in the string with numbers.
ex. 'a': 0, 'e': 1, 'i': 2, 'o':3, 'u':4
"""


def vowels_to_number(vowels):
    """Convert vowels to number."""
    return {'a': 0, 'e': 1, 'i': 2, 'o':3, 'u':4}[vowels]


def number_to_vowels(number):
    """Convert number to vowels."""
    return {0: 'a', 1: 'e', 2:'i', 3:'o', 4:'u'}[number]


def removeVowels(word):
	letters = []
	for c in word:
		if c.lower() in ('a','e','i','o','u'):
			letters.append(str(vowels_to_number(c)))
		else:
			letters.append(c)
	return ''.join(letters)

test = removeVowels('sunil')
print(test)
