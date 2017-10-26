# enter number
# greet user accordingly
# if it's divided by 3 print captain america
# if it's divided by 5 print iron man
# if divided by both 3 and 5 print civil war.

print("Welcome to Civil War I")

game_count = int(input('Enter no of games:'))

num = int(input('Enter number:'))

if num % 3 == 0 and num % 5 == 0:
	print('its civil war')
elif num % 5 == 0:
	print("team iron man")
elif num % 3 == 0:
	print("team captain")
else:
	print("patch up")