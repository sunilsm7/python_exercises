"""
    Make a functio aardvark that, given a string , returns 'aardvark'
    if the string starts with an a. Otherwise, return 'zebra'.

    >>>> aardvark("arg")
    aardvark

    >>>>aardvark("Trinket")
    zebra

"""

def aardvark(string):
    # addd code here that returns the answer
    if string[0] == 'a':
        return 'aardvark'
    else:
        return 'zebra'

# to check the function

print(aardvark("arg"))
print(aardvark("Trinket"))