import re

# list of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'


for pattern in patterns:
	print('Searching for {} in \n {}'.format(pattern ,text))

	# check for match
	if re.search(pattern, text):
		print("\t Match found.\n")
	else:
		print("\t No match found.\n")
