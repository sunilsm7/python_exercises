class Account(object): 

	def __init__(self, holder, number, balance, credit_line = 1500):
		self.Holder = holder
		self.Number = number
		self.Balance = balance
		self.Credit_line = credit_line

	def __str__(self):
		return "Account Holder:{}, number:{}, balance:{}".format(self.Holder, self.Number, self.Balance)

	def transfer(self, target, amount): 
		if (self.Balance - amount < self.Credit_line) :
			return False
		else:
			self.Balance -= amount
			target.Balance += amount
			return True 
 
	def deposit(self, amount): 
		self.Balance += amount 
 
	def withdraw(self, amount): 
		if (self.Balance - amount < self.Credit_line) :
			return False
		else:
			self.Balance -= amount
			return True
 
	def balance(self): 
		return self.Balance


