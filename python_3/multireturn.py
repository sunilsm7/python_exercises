"""
	Returning multiple values from Function

	We can return multiple values from function using the return statement by separating them with  a comma ( ,).
 	Multiple values are returned as tuples.
"""

def bigger(a, b):
	if a > b:
		return a, b
	else:
		return b, a

s =bigger(12,100)
print(s)
print(type(s))
