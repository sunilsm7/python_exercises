import re

text = open('shakespeare.txt')

for line in text:
    line = line.rstrip()
    if re.search('^[A-Z]{3,6}.*', line):
        print(line)
