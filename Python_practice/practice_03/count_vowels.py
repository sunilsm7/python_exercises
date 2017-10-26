"""
Count Vowels - Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
"""

def count_vowel(string, s):
	count = 0
	for i in string:
		if i == s:
			count += 1
	return count


def vowel_test(string):
	each_vowels_count = {}
	for i in string:
		if i.lower() in ('a','i','o','u','e'):
			each_vowels_count[i] = count_vowel(string, i)  # strings.count(i)
	return each_vowels_count

string = 'adbkjaqwriobviwibkvuwlewbewbk'
result = vowel_test(string)
print('each vowels count: {}'.format(result))
