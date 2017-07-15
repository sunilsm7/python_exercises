"""
    slicing
    list[start:stop:step]
    Make a function reverse_string that, given a string
    returns that string in reverse

    >>>> reverse_string("arg")
    gra
    >>>> reverse_string("Hii!")
    !iiH
"""

def reverse_string(string):
    return string[::-1]

print(reverse_string("args"))
print(reverse_string("Hiii!"))