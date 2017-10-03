"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

def tellAge(name, age):
	year = str((2017-age)+100)
	return name,age,year


name = input('Enter name:')
age = int(input('Enter your age:'))

result = tellAge(name, age)

print("Hi {}!. now you're: {}years old. You'll be 100years old on {}".format(result[0], result[1], result[2]))


