"""
	There are two ways to pass arguments to method: positional arguments and Keyword arguments. We have already seen how positional arguments work in the previous section. In this section we will learn about keyword arguments.

Keyword arguments allows you to pass each arguments using name value pairs like this   name=value . Let’s take an example:
"""

def named_args(name, greeting):
	print(greeting + " " + name)

named_args(name='jim', greeting='hello')