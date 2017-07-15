"""
    Make a function commafy that, given a list of three or more things.
    returns a list with commas.
    >>> commafy(["trinket","learnig","fun"])
        trinket,learnig,fun
    >>> commafy(["lions", "tigers","bears"])
        lions, tigers, bears
"""

def commafy(list):
    
    # add code here
    list[-1] = "and " + list[-1]
    return ', '.join(list)

# check code

print(commafy(["trinket","learnig","fun"]))
print(commafy(["lions", "tigers","bears"]))
