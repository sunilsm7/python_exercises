"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors >> 0
Scissors beats paper >> 1
Paper beats rock  >> 2

"""
print(""" Pick one >>
	rock: 0,
	paper: 1,
	scissors: 2
	""")

user1 = input('User1 choice:')
user2 = input('User2 choice:')

def choice_to_number(choice):
    """Convert choice to number."""
    
    return {'rock': 0, 'paper': 1, 'scissors': 2}[choice]


def number_to_choice(number):
    """Convert number to choice."""
    
    return {0: 'rock', 1: 'paper', 2:'scissors'}[number]


def addLine():
	print("-------------------------------------------------")


def checkResults(user1,user2):
	addLine()
	if user1 in ('0','1', '2') and user2 in ('0','1', '2'):
		user1_choice_number = int(user1)
		user2_choice_number = int(user2)
	else:
		user1_choice_number = choice_to_number(user1)
		user2_choice_number = choice_to_number(user2)

	if user1_choice_number == user2_choice_number:

		return "It's Tie"
	elif (user1_choice_number - user2_choice_number)%3 == 1:
		return 'user1 wins!!!'
	else:
		return 'user2 wins!!!'



result = checkResults(user1, user2)
print(result)
addLine()
