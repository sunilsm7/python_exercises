"""
    Make a function gerund_infinitive that, given a string
    returns the rest of the string prefixed with "to". If that
    doesn't end in "ing", return "That's not a gerund!"

    >>>> gerund_infinitive("building")
    to build
    >>>> gerund_infinitive("build")
"""

def gerund_infinitive(string):
    # Add code here
    if string[-3:] == 'ing':
        
        return  "to " +string[:-3]
    else:
        return "That's not a gerund!"

# Add statements to test the code

print(gerund_infinitive("building"))
print(gerund_infinitive("build"))