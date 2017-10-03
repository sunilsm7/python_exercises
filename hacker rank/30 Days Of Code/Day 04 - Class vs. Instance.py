"""
In this challenge, we're going to learn about the difference between a class and an instance;
because this is an Object Oriented concept, it's only enabled in certain languages.

Task
Write a Person class with an instance variable, age, and a constructor that takes an integer, initial_age, as a parameter.
The constructor must assign initial_age to _age after confirming the argument passed as _initial_age is not negative.
If a negative argument is passed as initial_age, the constructor should set to and print "Age is not valid, setting age to 0."

In addition, you must write the following instance methods:
	age_1_year() should increase the instance variable _age by 1.
	is_old() should perform the following conditional actions:
		If age < 13, print "You are young.".
		If age >= 13 and age < 18, print "You are a teenager.".
		Otherwise, print "You are old.".
"""
