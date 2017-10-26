""" 
	split with regular expressions.
"""
import re

# term to split
split_term = ':'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

# split the phrase
result = re.split(split_term, phrase)
print(result)

