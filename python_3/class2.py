# Hiding data fields
class BankAccount:
	# constructor or initializer
	def __init__(self, name, money):
		self.__name = name
		self.__balance = money # __balance is private now, so it is only accessible inside the class

	def deposit(self, money):
		self.__balance += money


	def withdraw(self, money):
		if self.__balance > money:
			self.__balance -= money
		else:
			return "Insufficient funds"

	def checkbalance(self):
		return self.__balance


name = input('Enter name:')
amount = int(input('Enter Amount:'))
b1 = BankAccount(name, amount)
print('Current balance:',b1.checkbalance())
withdraw_amt = int(input('amount to withdraw:'))
print(b1.withdraw(withdraw_amt))
print('Current balance:',b1.checkbalance())
deposit_amt = int(input('amount to deposit'))
b1.deposit(deposit_amt)
print('Current balance:',b1.checkbalance())

# try to access __balance data field outside of class
#print(b1.__balance)