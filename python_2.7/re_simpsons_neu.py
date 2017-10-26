"""
 find the first name of person, whose last name is 'Neu' and first name starts with a J.
"""

import re

fh = open('simpsons_phone_book.txt')
for line in fh:
	if re.search(r".*Simpsons", line):
		print(line.rstrip())

fh.close()