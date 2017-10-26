import re

def multi_re_find(patterns, phrase):
	''' takes list of regex patterns and print all matches list '''
	for pattern in patterns:
		print('Searching the phrase using the re check: {}'.format(pattern))
		print(re.findall(pattern, phrase))
		print('\n')