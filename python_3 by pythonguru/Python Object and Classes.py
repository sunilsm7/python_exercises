Python Object and Classes
4 Replies
Get started learning Python with DataCamp's free Intro to Python tutorial. Learn Data Science by completing interactive coding challenges and watching videos by expert instructors. Start Now!

Creating object and classes

Python is an object-oriented language. In python everything is object i.e int , str , bool  even modules, functions are also objects.

Object oriented programming use objects to create programs, and these objects stores data and behaviors.

Defining class

Class name in python is preceded with class  keyword followed by colon ( : ). Classes commonly contains data field to store the data and methods for defining behaviors. Also every class in python contains a special method called initializer (also commonly known as constructors), which get invoked automatically every time new object is created.

Let’s see an example.


class Person:

       # constructor or initializer
      def __init__(self, name): 
            self.name = name # name is data field also commonly known as instance variables

      # method which returns a string
     def whoami(self):
           return "You are " + self.name
1
2
3
4
5
6
7
8
9
class Person:
 
       # constructor or initializer
      def __init__(self, name): 
            self.name = name # name is data field also commonly known as instance variables
 
      # method which returns a string
     def whoami(self):
           return "You are " + self.name
 

here we have created a class called Person  which contains one data field called name  and method whoami().

What is self ??

All methods in python including some special methods like initializer have first parameter self . This parameter refers to the object which invokes the method. When you create new object the self parameter in the __init__  method is automatically set to reference the object you have just created.

Creating object from class


p1 = Person('tom') # now we have created a new person object p1
print(p1.whoami())
print(p1.name)
1
2
3
p1 = Person('tom') # now we have created a new person object p1
print(p1.whoami())
print(p1.name)

Expected Output:


You are tom
tom
1
2
You are tom
tom
Note: When you call a method you don’t need to pass anything to self  parameter, python automatically does that for you behind the scenes.

You can also change the name  data field.


p1.name = 'jerry'
print(p1.name)
1
2
p1.name = 'jerry'
print(p1.name)
Expected Output:


jerry
1
jerry
Although it is a bad practice to give access to your data fields outside the class. We will discuss how to prevent this next.

Hiding data fields

To hide data fields you need to define private data fields. In python you can create private data field using two leading underscores. You can also define a private method using two leading underscores.

Let’s see an example


class BankAccount:

     # constructor or initializer
    def __init__(self, name, money):
         self.__name = name
         self.__balance = money   # __balance is private now, so it is only accessible inside the class

    def deposit(self, money):
         self.__balance += money

    def withdraw(self, money):
         if self.__balance > money :
             self.__balance -= money
             return money
         else:
             return "Insufficient funds"

    def checkbalance(self):
         return self.__balance

b1 = BankAccount('tim', 400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.checkbalance())
print(b1.withdraw(800))
print(b1.checkbalance())
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
class BankAccount:
 
     # constructor or initializer
    def __init__(self, name, money):
         self.__name = name
         self.__balance = money   # __balance is private now, so it is only accessible inside the class
 
    def deposit(self, money):
         self.__balance += money
 
    def withdraw(self, money):
         if self.__balance > money :
             self.__balance -= money
             return money
         else:
             return "Insufficient funds"
 
    def checkbalance(self):
         return self.__balance
 
b1 = BankAccount('tim', 400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.checkbalance())
print(b1.withdraw(800))
print(b1.checkbalance())
Expected Output:


Insufficient funds
900
800
100
1
2
3
4
Insufficient funds
900
800
100
Let’s try to access __balance  data field outside of class.


print(b1.__balance)
1
print(b1.__balance)
Expected Output:


AttributeError: 'BankAccount' object has no attribute '__balance'
1
AttributeError: 'BankAccount' object has no attribute '__balance'
As you can see now __balance  is not accessible outside the class.

In next chapter we will learn about operator overloading.

