import random
n = 20
to_be_guessed = int(n*random.random()) + 1
guess = 0

while guess != to_be_guessed:
	guess = int(input('Enter number:'))
	if guess > 0:
		if guess > to_be_guessed:
			print("it's too large")
		else:
			print("it's too small")
	else:
		print("you've give up")
		break
else:
	print("Congratulations")
