"""
 Plot: Usain Bolt, you and Qazi
 had a race, Surprisingly, Usain bolt won.
 You came in 2nd and Qazi came in 3rd :(.

 Can you think of a way to write a function
 that given a person's name, returns his/her place ?

 ALso

 Can you think of a way to write a function
 that given a place, returns his/her name ?

 Write 2 Functions

 One that converts choice to number
 and
 One that converts number to choice.

"""

def choice_to_number(choice):
    """ Convert choice to number ."""
    # If choice is Usain you should get back 1.
    return {'Usain': 1, 'Sunil': 2, 'Qazi': 3}[choice]
    
#print(choice_to_number('Sunil'))

def number_to_choice(number):
    """ Convert number to choice """
    return {1: 'Usain', 2: 'Sunil', 3: 'Qazi'}[number]

#print(number_to_choice(2))

def test_choice_to_number():
    assert choice_to_number("Usain") == 1
    assert choice_to_number("Sunil") == 2
    assert choice_to_number("Qazi") == 3

def test_number_to_choice():
    assert number_to_choice(1) == 'Usain'
    assert number_to_choice(2) == 'Sunil'
    assert number_to_choice(3) == 'Qazi'

def test_all():

    try:
        test_choice_to_number()
        test_number_to_choice()

    except AssertionError:
        import wrong

    else:
        import success

test_all()

