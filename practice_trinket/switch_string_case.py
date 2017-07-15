"""
    Make a function switch_case that, give a string, 
    returns the string with uppercase letters in lowercase
    and vice-versa. Include punction and other non-cased 
    characters unchanged.

    >>>>switch_case("Arg!)
    aRG!
    >>>> switch_case("TrInKeT")
"""

def switch_case(string):
    # Add code here that returns the answer
    new_string = ''
    for letter in string:
        if letter.islower():
            new_string +=letter.upper()
        else:
            new_string +=letter.lower()
        
    return new_string


# check the function

print(switch_case("Arg!"))
print(switch_case("TrIKeT"))