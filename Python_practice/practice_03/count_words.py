string = """
Count Words in a String, Count the number of individual words in a string.
For added complexity read these string in from a text file and generate a summary.
"""

def words_count(string):
	each_word_count = {}
	words_list = string.split()
	word_count = len(words_list)
	for word in words_list:
		each_word_count[word] = words_list.count(word)
	return each_word_count

result = words_count(string)
print(result)