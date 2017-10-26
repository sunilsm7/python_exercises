import re
fh = open("tags.txt")
for i in fh:
	res = re.search(r"<([a-z]+)>(.*)</\1>", i)
	print(res.group(1) + ": " + res.group(2))

fh.close()