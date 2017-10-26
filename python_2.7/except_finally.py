def askint():
	while True:
		try:
			val = int(raw_input("Please enter an integer: "))

		except:
			print("Looks like you did not enter an integer!")
			continue
		else:
			print('its integer')
			exit()
		finally:
			print("Finally block")
		print(val)

askint()