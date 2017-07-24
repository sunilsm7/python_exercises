
"""
	It is possible to mix positional arguments and Keyword arguments,
	but for this positional argument must appear before any Keyword arguments
	Let’s see this through an example.
"""

def my_func(a, b, c):
	print(a, b, c)

#using positional arguments only
print("only positional arguments",my_func(12,13,14))

# here first argument is passed as positional arguments while other two as keyword 
print("first args is positional and remaining named keyword", my_func(12, b=15, c=14))